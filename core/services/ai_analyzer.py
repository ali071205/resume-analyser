"""
AI Analyzer Service — Uses Google Gemini API (new SDK) for resume analysis.
Performs skill extraction, gap analysis, scoring, classification, and recommendations.
"""

import json
import re
try:
    from google import genai
except ImportError:
    genai = None

from django.conf import settings


class SkillAnalyzer:
    """
    AI-powered resume analysis engine using Google Gemini API (new google-genai SDK).
    """

    # Using latest 2026 models found in user's account
    MODELS = [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-flash-latest",
        "gemini-pro-latest",
    ]

    def __init__(self):
        """Initialize the Gemini client."""
        if genai is not None:
            self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def analyze_resume(self, resume_text, job_description, job_title=""):
        """
        Complete analysis pipeline with automatic model fallback.
        """
        if genai is None:
            return self._get_fallback_result("The 'google-genai' library is not installed. Please run: pip install google-genai")

        prompt = self._build_prompt(resume_text, job_description, job_title)

        errors = []
        for model_name in self.MODELS:
            try:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                
                result_text = response.text.strip()

                # Clean up markdown code blocks if present
                result_text = re.sub(r'^```json\s*', '', result_text)
                result_text = re.sub(r'^```\s*', '', result_text)
                result_text = re.sub(r'\s*```$', '', result_text)
                result_text = result_text.strip()

                try:
                    result = json.loads(result_text)
                    return self._validate_result(result)
                except json.JSONDecodeError as json_err:
                    errors.append(f"{model_name}: JSON Parse Error - {str(json_err)}\nResponse was: {result_text[:100]}...")
                    continue

            except Exception as e:
                errors.append(f"{model_name}: {str(e)}")
                continue

        # All models failed
        error_msg = " | ".join(errors)
        return self._get_fallback_result(error_msg)

    def _build_prompt(self, resume_text, job_description, job_title):
        """Build the analysis prompt."""
        return f"""You are an expert HR consultant and technical recruiter with 15 years of experience.
Analyze the following resume against the provided job description.

RESUME TEXT:
\"\"\"
{resume_text[:4000]}
\"\"\"

JOB TITLE: {job_title if job_title else "Not specified"}

JOB DESCRIPTION:
\"\"\"
{job_description[:2500]}
\"\"\"

Provide a comprehensive analysis in the following EXACT JSON format.
Do NOT include any text outside the JSON. Do NOT use markdown code blocks.
Return ONLY the raw JSON object:

{{
    "overall_score": <number between 0 and 100>,
    "category": "<one of: frontend, backend, fullstack, ml, devops, data, mobile, other>",
    "resume_skills": ["<list of ALL skills found in the resume>"],
    "required_skills": ["<list of ALL skills required by the job description>"],
    "matched_skills": ["<skills that match between resume and JD>"],
    "missing_skills": ["<skills required by JD but missing from resume>"],
    "strengths": ["<3-5 key strengths of this candidate for this role>"],
    "detailed_feedback": "<A detailed 3-4 paragraph analysis of how well the candidate fits the role, areas of strength, gaps to address, and overall recommendation>",
    "recommendations": [
        {{
            "title": "<Project or course name to fill the skill gap>",
            "description": "<Brief description of what to learn/build>",
            "skill_target": "<Which missing skill this addresses>"
        }}
    ],
    "skill_scores": {{
        "<skill_name>": <candidate proficiency 0-100>,
        "...repeat for top 8 skills..."
    }},
    "required_scores": {{
        "<skill_name>": <required proficiency 0-100>,
        "...same skills as skill_scores..."
    }}
}}

RULES:
1. skill_scores and required_scores MUST have the SAME keys.
2. Include 6-8 skills in skill_scores and required_scores.
3. recommendations should have 3-5 items.
4. All skills should be properly capitalized.
5. overall_score should reflect genuine match quality.
"""

    def _validate_result(self, result):
        """Validate and sanitize the AI response."""
        defaults = {
            'overall_score': 0,
            'category': 'other',
            'resume_skills': [],
            'required_skills': [],
            'matched_skills': [],
            'missing_skills': [],
            'strengths': [],
            'detailed_feedback': '',
            'recommendations': [],
            'skill_scores': {},
            'required_scores': {},
        }

        for key, default in defaults.items():
            if key not in result:
                result[key] = default

        # Ensure score is in valid range
        result['overall_score'] = max(0, min(100, float(result['overall_score'])))

        # Ensure category is valid
        valid_categories = ['frontend', 'backend', 'fullstack', 'ml', 'devops', 'data', 'mobile', 'other']
        if result['category'] not in valid_categories:
            result['category'] = 'other'

        # Ensure skill_scores and required_scores have same keys
        all_skills = set(list(result['skill_scores'].keys()) + list(result['required_scores'].keys()))
        for skill in all_skills:
            if skill not in result['skill_scores']:
                result['skill_scores'][skill] = 0
            if skill not in result['required_scores']:
                result['required_scores'][skill] = 0

        return result

    def _get_fallback_result(self, error_msg):
        """Return a fallback result when all AI models fail."""
        return {
            'overall_score': 0,
            'category': 'other',
            'resume_skills': [],
            'required_skills': [],
            'matched_skills': [],
            'missing_skills': [],
            'strengths': [],
            'detailed_feedback': f'Analysis could not be completed. Error details: {error_msg}. Please check your API key and quotas.',
            'recommendations': [],
            'skill_scores': {},
            'required_scores': {},
        }
