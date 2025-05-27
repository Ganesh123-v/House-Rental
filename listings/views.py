from django.shortcuts import render, get_object_or_404
from .models import House

def house_list(request):
    houses = House.objects.filter(available=True).order_by('-created_at')
    return render(request, 'listings/house_list.html', {'houses': houses})

def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, 'listings/house_detail.html', {'house': house})
