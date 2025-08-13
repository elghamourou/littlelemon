from django.http import HttpResponse
from django.shortcuts import render

from restaurant.models import Booking
from restaurant.serializers import BookingSerializer
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
