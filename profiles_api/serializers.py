from rest_framework import serializers

#Sirve para poder convertir json a python y python a json
class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)