# models.py

from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.IntegerField()
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name


# One-to-one relationship
class StudentProfile(models.Model):
    bio = models.TextField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.student.name
