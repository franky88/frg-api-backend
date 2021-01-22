from students.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'extension_name', 'get_fullname', 'birth_date', 'calculate_age', 'date_register', 'date_updated', 'parent_email', 'parent_contact']