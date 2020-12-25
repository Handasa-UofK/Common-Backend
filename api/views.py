from django.shortcuts import render
from rest_framework import generics
from .models import Department, Assignment, Lecture
from .serializers import DepartmentSerizalizer, AssignmentSerializer, LectureSerializer

# Create your views here.
class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects
    serializer_class = DepartmentSerizalizer


class AssignmentListView(generics.ListAPIView):
    queryset = Assignment.objects
    serializer_class = AssignmentSerializer



class LectureListView(generics.ListAPIView):
    queryset = Lecture.objects
    serializer_class = LectureSerializer