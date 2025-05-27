from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available', 'created_at')
    list_filter = ('available',)
    search_fields = ('title', 'address')
