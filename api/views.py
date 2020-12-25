from django.shortcuts import render
from rest_framework import generics
from .models import Department
from .serializers import DepartmentSerizalizer

# Create your views here.
class DepartmentListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerizalizer