from rest_framework import serializers
from ..models import Subject
from ..models import Course, Module, Content


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "title", "slug"]
