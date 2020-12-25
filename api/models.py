from django.db import models
from django.core import validators

Days = (
    ("Sun", "Sunday"),
    ("Mon", "Monday"),
    ("Tue", "Tuesday"),
    ("Wed", "Wednesday"),
    ("Thu", "Thursday"),
    ("Fri", "Friday"),
    ("Sat", "Saturday"),

)

class Batch(models.Model):
    code = models.CharField(max_length=3)
    def __str__(self):
        return self.code

class Department(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    batch = models.ForeignKey(Batch, on_delete= models.CASCADE)
    phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    Department = models.ForeignKey(Department, on_delete = models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=10)
    link = models.TextField()
    batch = models.ForeignKey(Batch, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    day = models.CharField(choices= Days, default=1, max_length=10)
    duration = models.FloatField()
    time =  models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.subject.name + " " + self.day

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    deadline = models.DateField(auto_now_add=False, auto_created= False, auto_now= False)
    description = models.TextField()
