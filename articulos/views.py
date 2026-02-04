from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Articulo
from .serializers import ArticuloSerializer
from  rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def articulo_lista(request):
    if  request.method == 'GET':
          autores = Articulo.objects.all()
          serializer = ArticuloSerializer(autores, many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def articulo_detalle(request,pk):
    libro = get_object_or_404(Articulo, pk=pk)
   
    if request.method == 'GET':
        serializer = ArticuloSerializer(libro)
        return Response (serializer.data)
    
    
    elif request.method == 'DELETE':
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticuloSerializer(libro, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

