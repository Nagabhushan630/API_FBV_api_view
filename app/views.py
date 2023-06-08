from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def Details(request):
    eo=Employee.objects.all()
    ed=EmployeeMS(eo,many=True)
    return Response(ed.data)