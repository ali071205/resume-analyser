"""
Views for SkillSync AI — Handles all page rendering and form processing.
"""

import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse
from django.contrib import messages
from .models import Resume, AnalysisResult
from .forms import ResumeUploadForm
from .services.pdf_parser import extract_text
from .services.ai_analyzer import SkillAnalyzer
from .services.report_generator import generate_analysis_report


def landing_view(request):
    """Landing page with hero section and features."""
    total_analyses = AnalysisResult.objects.count()
    total_resumes = Resume.objects.count()
    
    context = {
        'total_analyses': total_analyses,
        'total_resumes': total_resumes,
    }
    return render(request, 'core/landing.html', context)


def upload_view(request):
    """Handle resume upload and trigger AI analysis."""
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['resume_file']
            job_description = form.cleaned_data['job_description']
            job_title = form.cleaned_data.get('job_title', '')
            
            # Determine file type
            file_ext = uploaded_file.name.rsplit('.', 1)[-1].lower()
            
            # Save resume to database
            resume = Resume(
                file=uploaded_file,
                original_filename=uploaded_file.name,
                file_type=file_ext,
            )
            resume.save()
            
            try:
                # Extract text from the uploaded file
                extracted_text = extract_text(resume.file.path, file_ext)
                resume.extracted_text = extracted_text
                resume.save()
                
                if not extracted_text.strip():
                    messages.error(request, 'Could not extract text from the resume. Please ensure the file contains readable text.')
                    return redirect('upload')
                
                # Run AI analysis
                analyzer = SkillAnalyzer()
                result = analyzer.analyze_resume(extracted_text, job_description, job_title)
                
                # Check if AI analysis actually succeeded
                feedback = result.get('detailed_feedback', '')
                if result.get('overall_score', 0) == 0 and ('error' in feedback.lower() or 'could not' in feedback.lower() or 'rate-limited' in feedback.lower()):
                    messages.error(request, 'AI analysis failed due to API rate limits. Please wait 1 minute and try again.')
                    resume.delete()  # Clean up the failed upload
                    return redirect('upload')
                
                # Save analysis results
                analysis = AnalysisResult(
                    resume=resume,
                    job_description=job_description,
                    job_title=job_title,
                    overall_score=result.get('overall_score', 0),
                    category=result.get('category', 'other'),
                    detailed_feedback=result.get('detailed_feedback', ''),
                )
                
                # Set JSON fields using property setters
                analysis.matched_skills = result.get('matched_skills', [])
                analysis.missing_skills = result.get('missing_skills', [])
                analysis.resume_skills = result.get('resume_skills', [])
                analysis.required_skills = result.get('required_skills', [])
                analysis.recommendations = result.get('recommendations', [])
                analysis.strengths = result.get('strengths', [])
                analysis.skill_scores = result.get('skill_scores', {})
                analysis.required_scores = result.get('required_scores', {})
                
                analysis.save()
                
                return redirect('dashboard', analysis_id=analysis.id)
                
            except Exception as e:
                messages.error(request, f'Analysis failed: {str(e)}. Please try again.')
                return redirect('upload')
    else:
        form = ResumeUploadForm()
    
    return render(request, 'core/upload.html', {'form': form})


def dashboard_view(request, analysis_id):
    """Display analysis results with charts and skill data."""
    analysis = get_object_or_404(AnalysisResult, id=analysis_id)
    
    # Prepare chart data for JavaScript
    skill_scores = analysis.skill_scores
    required_scores = analysis.required_scores
    
    chart_labels = list(skill_scores.keys()) if skill_scores else []
    chart_current = [skill_scores.get(s, 0) for s in chart_labels]
    chart_required = [required_scores.get(s, 0) for s in chart_labels]
    
    context = {
        'analysis': analysis,
        'matched_skills': analysis.matched_skills,
        'missing_skills': analysis.missing_skills,
        'resume_skills': analysis.resume_skills,
        'strengths': analysis.strengths,
        'recommendations': analysis.recommendations,
        'chart_labels': json.dumps(chart_labels),
        'chart_current': json.dumps(chart_current),
        'chart_required': json.dumps(chart_required),
        'overall_score': analysis.overall_score,
    }
    
    return render(request, 'core/dashboard.html', context)


def history_view(request):
    """List all past analyses."""
    analyses = AnalysisResult.objects.select_related('resume').all()[:20]
    return render(request, 'core/history.html', {'analyses': analyses})


def download_report_view(request, analysis_id):
    """Generate and download PDF report."""
    analysis = get_object_or_404(AnalysisResult, id=analysis_id)
    
    try:
        buffer = generate_analysis_report(analysis)
        filename = f"SkillSync_Report_{analysis.resume.original_filename.rsplit('.', 1)[0]}.pdf"
        
        return FileResponse(
            buffer,
            as_attachment=True,
            filename=filename,
            content_type='application/pdf',
        )
    except Exception as e:
        messages.error(request, f'Failed to generate report: {str(e)}')
        return redirect('dashboard', analysis_id=analysis_id)


def api_chart_data(request, analysis_id):
    """API endpoint for chart data (AJAX)."""
    analysis = get_object_or_404(AnalysisResult, id=analysis_id)
    
    skill_scores = analysis.skill_scores
    required_scores = analysis.required_scores
    
    labels = list(skill_scores.keys())
    
    data = {
        'labels': labels,
        'current': [skill_scores.get(s, 0) for s in labels],
        'required': [required_scores.get(s, 0) for s in labels],
        'overall_score': analysis.overall_score,
        'matched_count': len(analysis.matched_skills),
        'missing_count': len(analysis.missing_skills),
        'category': analysis.get_category_display(),
    }
    
    return JsonResponse(data)
