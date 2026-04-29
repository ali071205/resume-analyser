"""
Models for SkillSync AI — Resume analysis data storage.
"""

from django.db import models
import json


class Resume(models.Model):
    """Stores uploaded resume files and their extracted text."""
    file = models.FileField(upload_to='resumes/')
    original_filename = models.CharField(max_length=255)
    extracted_text = models.TextField(blank=True, default='')
    file_type = models.CharField(max_length=10, default='pdf')  # pdf or docx
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.original_filename} ({self.uploaded_at.strftime('%Y-%m-%d %H:%M')})"


class AnalysisResult(models.Model):
    """Stores AI analysis results for a resume vs job description comparison."""
    
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend Developer'),
        ('backend', 'Backend Developer'),
        ('fullstack', 'Full-Stack Developer'),
        ('ml', 'ML/AI Engineer'),
        ('devops', 'DevOps Engineer'),
        ('data', 'Data Scientist'),
        ('mobile', 'Mobile Developer'),
        ('other', 'Other'),
    ]
    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='analyses')
    job_description = models.TextField()
    job_title = models.CharField(max_length=255, blank=True, default='')
    
    # Scores
    overall_score = models.FloatField(default=0)  # 0-100
    
    # Skills Data (stored as JSON)
    matched_skills_json = models.TextField(default='[]')
    missing_skills_json = models.TextField(default='[]')
    resume_skills_json = models.TextField(default='[]')
    required_skills_json = models.TextField(default='[]')
    
    # Classification
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    
    # AI Feedback
    detailed_feedback = models.TextField(blank=True, default='')
    recommendations_json = models.TextField(default='[]')
    strengths_json = models.TextField(default='[]')
    
    # Skill proficiency scores for charts (JSON: {"Python": 85, "Django": 70, ...})
    skill_scores_json = models.TextField(default='{}')
    required_scores_json = models.TextField(default='{}')
    
    analyzed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-analyzed_at']

    def __str__(self):
        return f"Analysis for {self.resume.original_filename} - Score: {self.overall_score}"

    # Property helpers for JSON fields
    @property
    def matched_skills(self):
        try:
            return json.loads(self.matched_skills_json)
        except (json.JSONDecodeError, TypeError):
            return []

    @matched_skills.setter
    def matched_skills(self, value):
        self.matched_skills_json = json.dumps(value)

    @property
    def missing_skills(self):
        try:
            return json.loads(self.missing_skills_json)
        except (json.JSONDecodeError, TypeError):
            return []

    @missing_skills.setter
    def missing_skills(self, value):
        self.missing_skills_json = json.dumps(value)

    @property
    def resume_skills(self):
        try:
            return json.loads(self.resume_skills_json)
        except (json.JSONDecodeError, TypeError):
            return []

    @resume_skills.setter
    def resume_skills(self, value):
        self.resume_skills_json = json.dumps(value)

    @property
    def required_skills(self):
        try:
            return json.loads(self.required_skills_json)
        except (json.JSONDecodeError, TypeError):
            return []

    @required_skills.setter
    def required_skills(self, value):
        self.required_skills_json = json.dumps(value)

    @property
    def recommendations(self):
        try:
            return json.loads(self.recommendations_json)
        except (json.JSONDecodeError, TypeError):
            return []

    @recommendations.setter
    def recommendations(self, value):
        self.recommendations_json = json.dumps(value)

    @property
    def strengths(self):
        try:
            return json.loads(self.strengths_json)
        except (json.JSONDecodeError, TypeError):
            return []

    @strengths.setter
    def strengths(self, value):
        self.strengths_json = json.dumps(value)

    @property
    def skill_scores(self):
        try:
            return json.loads(self.skill_scores_json)
        except (json.JSONDecodeError, TypeError):
            return {}

    @skill_scores.setter
    def skill_scores(self, value):
        self.skill_scores_json = json.dumps(value)

    @property
    def required_scores(self):
        try:
            return json.loads(self.required_scores_json)
        except (json.JSONDecodeError, TypeError):
            return {}

    @required_scores.setter
    def required_scores(self, value):
        self.required_scores_json = json.dumps(value)
