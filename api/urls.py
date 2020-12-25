from django.urls import path
from .views import DepartmentListView, AssignmentListView, LectureListView

urlpatterns = [
    path('departments', DepartmentListView.as_view()),
    path('assignments', AssignmentListView.as_view()),
    path('lectures', LectureListView.as_view())

]
