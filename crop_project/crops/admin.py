from django.contrib import admin
from .models import CropData

<<<<<<< HEAD
# Custom admin display for better table view
=======
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
@admin.register(CropData)
class CropDataAdmin(admin.ModelAdmin):
    list_display = ('year', 'region', 'crop', 'production', 'yield_amount')
    list_filter = ('year', 'region')
    search_fields = ('crop', 'region')