"""
Forms for SkillSync AI — Resume upload and job description input.
"""

from django import forms
from .models import Resume


class ResumeUploadForm(forms.Form):
    """Form for uploading a resume and entering a job description."""
    
    resume_file = forms.FileField(
        label='Upload Resume',
        help_text='Accepted formats: PDF, DOCX (Max 10MB)',
        widget=forms.FileInput(attrs={
            'id': 'resume-file-input',
            'accept': '.pdf,.docx',
            'class': 'file-input',
        })
    )
    
    job_title = forms.CharField(
        max_length=255,
        required=False,
        label='Job Title (Optional)',
        widget=forms.TextInput(attrs={
            'id': 'job-title-input',
            'placeholder': 'e.g., Senior Python Developer',
            'class': 'text-input',
        })
    )
    
    job_description = forms.CharField(
        label='Job Description',
        widget=forms.Textarea(attrs={
            'id': 'job-description-input',
            'placeholder': 'Paste the job description here...\n\nExample:\nWe are looking for a Python Developer with 3+ years of experience in Django, REST APIs, PostgreSQL, Docker, and CI/CD pipelines. Experience with machine learning frameworks (TensorFlow/PyTorch) is a plus.',
            'class': 'textarea-input',
            'rows': 8,
        })
    )
    
    def clean_resume_file(self):
        """Validate the uploaded file."""
        file = self.cleaned_data.get('resume_file')
        if file:
            # Check file extension
            ext = file.name.rsplit('.', 1)[-1].lower()
            if ext not in ['pdf', 'docx']:
                raise forms.ValidationError(
                    'Invalid file format. Please upload a PDF or DOCX file.'
                )
            
            # Check file size (10MB max)
            if file.size > 10 * 1024 * 1024:
                raise forms.ValidationError(
                    'File too large. Maximum size is 10MB.'
                )
        return file
