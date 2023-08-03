from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Train
from .serializers import TrainSerializer

class TrainListView(APIView):
    def get(self, request):
        trains = Train.objects.all()
        serializer = TrainSerializer(trains, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainDetailView(APIView):
    def get(self, request, pk):
        train = Train.objects.get(pk=pk)
        serializer = TrainSerializer(train)
        return Response(serializer.data)

    def put(self, request, pk):
        train = Train.objects.get(pk=pk)
        serializer = TrainSerializer(train, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        train = Train.objects.get(pk=pk)
        train.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)