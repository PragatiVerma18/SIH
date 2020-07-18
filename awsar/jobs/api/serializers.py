from rest_framework import serializers

from accounts.api.serializers import UserSerializer
from ..models import *


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ["id", "user", "title", "description", "location", "type", "category", "last_date",
                  "company_name", "vacancies", "doc_url", "summary", "website", "created_at", "filled", "salary"]


class ApplicantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Applicant
        fields = "__all__"
