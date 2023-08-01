from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def data(request):
    BooksData = Book.objects.all()
    serializers = BookSerializers(BooksData,many=True)
    return Response(serializers.data)


@api_view(['POST'])
def post(request):
    serializers = BookSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
   
    return Response(serializers.data)

@api_view(['PUT'])
def update(request,id):
    Book_obj = Book.objects.get(id=id)
    serializers = BookSerializers(instance=Book_obj,data=request.data)
    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)


@api_view(['DELETE'])
def delete(request,id):
    Bookobj = Book.objects.get(id=id)
    Bookobj.delete()
    return Response("data was deleted")

    