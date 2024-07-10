from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product

# Create your views here.


class index(APIView):
    def get(self, request, format=None):
        return Response('Hello World!')
    

@api_view(['GET'])
def ShowAll(request):
    return Response('Hello World!')