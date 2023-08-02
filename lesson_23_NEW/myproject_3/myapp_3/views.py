from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

import json
from .models import Book
from .serializers import BookSerializer

json_data = '{"title": "New Book", "author": "John Doe", "publication_date": "2022-01-01"}'
book_dict = json.loads(json_data)
serializer = BookSerializer(data=book_dict)
serializer.is_valid(raise_exception=True)
book = serializer.save()