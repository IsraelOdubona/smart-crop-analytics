from django.shortcuts import render
from django.db.models import Q, Sum, Avg
from .models import CropData
import json


<<<<<<< HEAD
# This function handles the main data table page
# It displays crop records and allows filtering + sorting

def data_page(request):
    # Get all crop records from the database
    crops = CropData.objects.all()

    # Get filter values from the URL (GET request)
=======
def home(request):
    crops = CropData.objects.all()

    # ✅ GET FILTER VALUES
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
    year = request.GET.get('year')
    region = request.GET.get('region')
    search = request.GET.get('search')
    sort = request.GET.get('sort')

<<<<<<< HEAD
    # Apply year filter if selected
=======
    # ✅ FILTERS 
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
    if year:
        crops = crops.filter(year=year)

    # Apply region filter if selected
    if region:
        crops = crops.filter(region=region)

    # Search by crop name or region name
    if search:
        crops = crops.filter(
            Q(crop__icontains=search) |
            Q(region__icontains=search)
        )

<<<<<<< HEAD
    # Sort results based on user selection
=======
    # This retains a copy BEFORE slicing for charts
    filtered = crops

    # ✅ SORT NEXT
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
    if sort == 'production':
        # Highest production first
        crops = crops.order_by('-production')
    elif sort == 'yield':
        # Highest yield first
        crops = crops.order_by('-yield_amount')

<<<<<<< HEAD
    # Get unique years and regions for dropdown filters
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()

    # Send data to the HTML template
    return render(request, 'crops/data.html', {
        'crops': crops,
        'years': years,
        'regions': regions,
    })


# This function handles the charts dashboard page
# It creates chart data based on filters selected by the user

def chart_page(request):
    # Start with all crop records
    crops = CropData.objects.all()

    # Get selected filter values from the charts page
    year = request.GET.get('year')
    region = request.GET.get('region')
    crop_name = request.GET.get('crop')

    # Apply year filter if selected
    if year:
        crops = crops.filter(year=year)

    # Apply region filter if selected
    if region:
        crops = crops.filter(region=region)

    # Apply crop filter if selected
    if crop_name:
        crops = crops.filter(crop=crop_name)

    # Get dropdown values for filter options
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()
    crop_names = CropData.objects.values_list('crop', flat=True).distinct()

    # CHART 1: Total production grouped by crop
    production_data = (
        crops.values('crop')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False)
        .order_by('-total_production')[:10]  # Top 10 crops only
    )

    # Extract labels and values for Chart.js
    production_labels = [item['crop'] for item in production_data]
    production_values = [item['total_production'] or 0 for item in production_data]

    # CHART 2: Average yield grouped by year
    yield_data = (
        crops.values('year')
        .annotate(avg_yield=Avg('yield_amount'))
        .filter(avg_yield__isnull=False)
        .order_by('year')
    )

    # Extract labels and values for yield chart
    yield_labels = [item['year'] for item in yield_data]
    yield_values = [float(item['avg_yield'] or 0) for item in yield_data]

    # CHART 3: Total production grouped by region
    region_data = (
        crops.values('region')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False, total_production__gt=0)
        .order_by('-total_production')
    )

    # Extract labels and values for region chart
    region_labels = [item['region'] for item in region_data]
    region_values = [item['total_production'] or 0 for item in region_data]

    # Convert Python lists into JSON so JavaScript can use them in Chart.js
    return render(request, 'crops/charts.html', {
        'years': years,
        'regions': regions,
        'crop_names': crop_names,

        'production_labels': json.dumps(production_labels),
        'production_values': json.dumps(production_values),

        'yield_labels': json.dumps(yield_labels),
        'yield_values': json.dumps(yield_values),

        'region_labels': json.dumps(region_labels),
        'region_values': json.dumps(region_values),
=======
    # ✅ SLICE (ONLY FOR TABLE)
    crops = crops[:50]

    # 🔹 DROPDOWNS
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()

    # =========================
    # 📊 CHART DATA (FILTERED DATA)
    # =========================

    # 🔹 Production by crop
    production_data = (
        filtered
        .values('crop')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False, total_production__gt=0)
        .order_by('-total_production')[:10]
    )

    production_labels = [item['crop'] for item in production_data]
    production_values = [item['total_production'] or 0 for item in production_data]

    # 🔹 Yield over time 
    yield_data = (
        filtered
        .values('year')
        .annotate(avg_yield=Avg('yield_amount'))
        .filter(avg_yield__isnull=False, avg_yield__gt=0)
        .order_by('year')
    )

    yield_labels = [item['year'] for item in yield_data]
    yield_values = [float(item['avg_yield']) for item in yield_data]

    # 🔹 Production by region
    region_data = (
        filtered
        .values('region')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False, total_production__gt=0)
        .order_by('-total_production')
    )

    region_labels = [item['region'] for item in region_data]
    region_values = [item['total_production'] for item in region_data]

    return render(request, 'crops/home.html', {
        'crops': crops,
        'years': years,
        'regions': regions,
        'production_labels': production_labels,
        'production_values': production_values,
        'yield_labels': yield_labels,
        'yield_values': yield_values,
        'region_labels': region_labels,
        'region_values': region_values
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
    })