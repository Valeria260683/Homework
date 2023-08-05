from rest_framework import viewsets
from .models import Publisher
from .serializers import PublisherSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.response import Response

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list_by_publisher(self, request, publisher_id=None):
        authors = self.queryset.filter(publisher__id=publisher_id)
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data)