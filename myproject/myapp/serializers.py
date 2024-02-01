"""Serializers for myapp."""

from rest_framework import serializers
from myapp.models import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_name', 'teacher']


class TeacherSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(read_only=True, many=True)
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'subjects']



class  StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['id', 'bio', 'student']




class StudentCreateSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer(read_only=True)
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True, required=False)
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade', 'subjects', 'profile']


class StudentUpdateSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer(read_only=True)
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True, required=False)
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade', 'subjects', 'profile']





class StudentRetrieveSerializer(serializers.ModelSerializer):
    # subjects = SubjectSerializer(many=True)
    # profile = StudentProfileSerializer()
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade', 'subjects', 'profile']
        depth = 1
