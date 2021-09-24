from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status #estados de respuesta
from rest_framework import viewsets

from profiles_api import serializers
# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, fromat= None):
        #Retorna las caracteristicas
        an_apiview = [
            'Usando methods HTTP como funcion (get, post, patch, put, deleted)',
            'visata usada por django',
            'Control de la logica de la app',
            'Esta mapeado manuealmente a las URLs',
        ]
        #Retorna la informacion en formato json
        #Solo se retorna un json si es un diccionario o lista
        return Response({
            'message': 'Primera view',
            'an_apiview': an_apiview
        })

    def post(self, request):#peticion envio de data

        #definicion de los datos 
        serializer = self.serializer_class(data = request.data)

        #valido o no 
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message: ': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk = None): #actualizar onjeto pk = None sirve para no actualizar por id
        return Response({'method': 'PUT'})        

    def patch(self, request, pk = None):
        #actualizacion parcial de un objeto
        return Response({'method': 'PATCH'})

    def delete(self, request, pk = None):
        return Response({'method': 'DELETE'}) 


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    #test API
    def list(self, request):
        a_viewset = [
            'Usa acciones (list, create, retriece, update, destroy',
            'Automaticamente mapea los URLs usando RRouters',
            'Funcionalidad si tanto codigo',
        ]
        return Response({'Message': 'Soy un viewset', 'a_viewset': a_viewset})
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola, bienvenido: {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk = None):
        #obtiene un objeto y el id
        return Response({'http_method': 'GET'})

    def update(self, request, pk = None):
        #obtiene un objeto y el id
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk = None):
        #obtiene un objeto y el id
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk = None):
        #obtiene un objeto y el id
        return Response({'http_method': 'DELETE'})