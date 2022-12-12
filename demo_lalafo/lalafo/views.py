from django.shortcuts import render
from rest_framework import generics
from .models import Product
from rest_framework import filters
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product', 'description']

    def get_queryset(self):
        try:
            return Product.objects.filter(id=self.kwargs['pk'])
        except:
            return Product.objects.all()
