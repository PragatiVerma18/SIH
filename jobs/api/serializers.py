from rest_framework import serializers

from accounts.api.serializers import UserSerializer
from ..models import *


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ["id", "user", "title", "description", "location", "type", "category", "last_date",
                  "company_name", "vacancies", "doc_url", "summary", 'qualification', 'experience', 'age_limit', "website", "filled", "salary", "tags", "job_for_women", "job_for_disabled", "created_at", "updated_at"]


class ApplicantSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # job = JobSerializer()

    class Meta:
        model = Applicant
        fields = ["id", "user", "employee", "job"]
        # depth = 1


class ApplicantDetailSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # job = JobSerializer()

    class Meta:
        model = Applicant
        fields = ["id", "employee"]
        depth = 1
