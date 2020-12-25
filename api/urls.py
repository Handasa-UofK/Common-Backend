from django.urls import path
from .views import DepartmentListView

urlpatterns = [
    path('department', DepartmentListView.as_view())
]
