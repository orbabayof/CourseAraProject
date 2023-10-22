from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class BookView(APIView):
     def get(self, request, pk):
          return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)

     def put(self, request, pk):
          return Response({"title":request.data.get('title')}, status.HTTP_200_OK)


     