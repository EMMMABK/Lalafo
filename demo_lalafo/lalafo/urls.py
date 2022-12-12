from django.urls import path, include
from .views import *


urlpatterns = [
    path('api/v1/product-info/<int:pk>', ProductListCreateAPIView.as_view()),
    path('api/v1/product-info/', ProductListCreateAPIView.as_view())
]