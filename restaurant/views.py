from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

