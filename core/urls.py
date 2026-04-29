"""
URL patterns for the SkillSync AI core app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('upload/', views.upload_view, name='upload'),
    path('dashboard/<int:analysis_id>/', views.dashboard_view, name='dashboard'),
    path('history/', views.history_view, name='history'),
    path('download/<int:analysis_id>/', views.download_report_view, name='download_report'),
    path('api/chart/<int:analysis_id>/', views.api_chart_data, name='api_chart_data'),
]
