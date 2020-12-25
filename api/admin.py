from django.contrib import admin
from .models import Department, Student, Batch, Subject, Assignment, Lecture

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Lecture)