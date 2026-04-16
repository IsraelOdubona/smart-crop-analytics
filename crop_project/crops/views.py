from django.shortcuts import render
from django.db.models import Q
from .models import CropData

def home(request):
    crops = CropData.objects.all()

    year = request.GET.get('year')
    region = request.GET.get('region')
    search = request.GET.get('search')
    sort = request.GET.get('sort')

    if year:
        crops = crops.filter(year=year)

    if region:
        crops = crops.filter(region=region)

    if search:
        crops = crops.filter(
            Q(crop__icontains=search) |
            Q(region__icontains=search)
        )

    if sort == 'production':
        crops = crops.order_by('-production')
    elif sort == 'yield':
        crops = crops.order_by('-yield_amount')

    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()

    return render(request, 'crops/home.html', {
        'crops': crops,
        'years': years,
        'regions': regions
    })