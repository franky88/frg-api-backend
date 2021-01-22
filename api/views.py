from students.models import Student
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer

# Create your views here


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-date_register')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
