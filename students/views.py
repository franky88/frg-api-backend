from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all().order_by('-date_register')
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]