from rest_framework.renderers import JSONRenderer
from .serializers import BookSerializer
from .models import Book
from django.http import HttpResponse

def my_view(request):
    book = Book.objects.create(title='Book Title', author='Book Author', publication_date='2022-01-01')

    serializer = BookSerializer(book)
    json_object = JSONRenderer().render(serializer.data)

    return HttpResponse(json_object, content_type='application/json')


