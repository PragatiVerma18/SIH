from django.urls import path
from .views import ApplicantStats, TimeStats

urlpatterns = [
    path('duration', TimeStats),
    path('applicants', ApplicantStats)
]
