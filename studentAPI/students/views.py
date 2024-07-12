from django.shortcuts import render
from rest_framework import generics
from .models import Students
from .serializers import StudentSerializer

# Create your views here.

class StudentCreate(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
