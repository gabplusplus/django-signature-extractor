from rest_framework import generics, permissions
from .models import ExtractSign
from .serializer import ExtractSignSerialzier


class ExtractCreate(generics.CreateAPIView):
    serializer_class = ExtractSignSerialzier
    permission_classes = [permissions.AllowAny,]
    queryset = ExtractSign.objects.all()


class ListFiles(generics.ListAPIView):
    serializer_class = ExtractSignSerialzier
    permission_classes = [permissions.AllowAny,]
    queryset = ExtractSign.objects.all()