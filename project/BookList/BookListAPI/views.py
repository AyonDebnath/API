from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse



# Create your views here.
@api_view(['GET', 'POST'])
def books(request):
    return Response('list of the books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message":"list of the books by " + author}, status.HTTP_200_OK)
        return Response({"message":"list of the books"}, status.HTTP_200_OK)

    def post(self, request):
        return Response({"title":request.data.get('title')}, status.HTTP_201_CREATED)

class Book(APIView):
    def get(self, request, pk):
        return Response({"message": "Single book with id " + str(pk)}, status.HTTP_200_OK)
    def put(self, request, pk):
        return Response({"title": request.data.get('title')}, status.HTTP_200_OK)
