import datetime
from datetime import date
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    extension_name = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateField()
    parent_contact = models.CharField(max_length=11, verbose_name="parent contact number")
    parent_email = models.EmailField(blank=True, null=True)
    date_register = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['last_name']
    def get_fullname(self):
        fullname = "%s %s"%(self.first_name, self.last_name)
        return fullname
    def calculate_age(self):
        today = date.today()
        born = self.birth_date
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age
    # def date_filter(self):
    #     return self.date_register.year
    def __str__(self):
        return self.get_fullname()
    