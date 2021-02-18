from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
# Create your views here.

class FacultyView(viewsets.ModelViewSet):
    queryset = Faculty.objects.all().using('college')
    serializer_class = FacultySerializer

    