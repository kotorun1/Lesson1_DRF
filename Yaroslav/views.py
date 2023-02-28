from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import YaroslavSerializer
from .models import Books

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/books-list/',
        'Detail View': '/book-detail/<str:pk>/',
        'Create': '/book-create/',
        'Update': '/book-update/<str:pk>/',
        'Delete': '/book-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['POST'])
def bookCreate(request):
    serializer = YaroslavSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['GET'])
def booksList(request):
    books = Books.objects.all().order_by('-id')
    serializer = YaroslavSerializer(books, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def bookDetail(request,pk):
    books = Books.objects.get(id=pk)
    serializer = YaroslavSerializer(books, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def bookUpdate(request, pk):
    book = Books.objects.get(id=pk)
    serializer = YaroslavSerializer(books, many=False)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def bookDelete(request,pk):
    book = Books.objects.get(id=pk)
    book.delete()

    return Response('Deleted Sucefful')