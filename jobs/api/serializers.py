from rest_framework import serializers
from profiles.serializers import EmployeeProfileSerializer
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
        fields = ["id", "employee", "job", "applied_at", "status"]

        # depth = 1


class ApplicantDetailSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # job = JobSerializer()

    class Meta:
        model = Applicant
        fields = ["id", "employee", "applied_at", "status"]
        depth = 1
        read_only_fields = ('id', 'applied_at')


class JobAppliedByEmployeeSerializer(serializers.ModelSerializer):
    # job_count = serializers.SerializerMethodField()

    class Meta:
        model = Applicant
        fields = ["id", "job", "applied_at", "status"]
        depth = 1
