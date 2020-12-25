from rest_framework import serializers
from .models import Department, Assignment, Subject, Lecture, Batch

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    batch = BatchSerializer(read_only=True)
    class Meta:
        model = Subject
        fields = "__all__"

class DepartmentSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only = True)
    class Meta:
        model = Assignment
        fields = "__all__"

class LectureSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only = True)
    class Meta:
        model = Lecture
        fields = "__all__"
