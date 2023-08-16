from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from .models import Booking, Menu
from django.contrib.auth.models import User
from .serializers import BookingSerializer, MenuSerializer
from .serializers import UserSerilizer
from rest_framework import generics
# from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerilizer
#     permission_classes = [IsAuthenticated]


class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class MenuView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    