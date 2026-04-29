"""
Admin configuration for SkillSync AI models.
"""

from django.contrib import admin
from .models import Resume, AnalysisResult


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('original_filename', 'file_type', 'uploaded_at')
    list_filter = ('file_type', 'uploaded_at')
    search_fields = ('original_filename',)
    readonly_fields = ('uploaded_at',)


@admin.register(AnalysisResult)
class AnalysisResultAdmin(admin.ModelAdmin):
    list_display = ('resume', 'job_title', 'overall_score', 'category', 'analyzed_at')
    list_filter = ('category', 'analyzed_at')
    search_fields = ('job_title', 'job_description')
    readonly_fields = ('analyzed_at',)
