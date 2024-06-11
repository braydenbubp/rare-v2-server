from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from models.tag import Tag

class TagView(ViewSet):
    def retrieve(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
      
    def list(self, request):
        tags = Tag.objects.all()
        
        serializer = TagSerializer(tags)
        return Response(serializer.data)
    
    def create(self, request):
        tag = Tag.objects.create(
          tag = request.data["tag"],
        )
        tag.save()
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag')
