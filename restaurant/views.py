from django.http import HttpResponse
from django.shortcuts import render

from restaurant.models import Booking, MenuItem
from restaurant.serializers import BookingSerializer, MenuItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello, world!")

def home(request):
    return render(request, 'index.html',{})

class BookingView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

class MenuItemView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors}, status=400)