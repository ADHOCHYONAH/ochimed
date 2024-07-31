from django.contrib import admin
from .models import Omegameds


class OmegamedsAdmin(admin.ModelAdmin):
    list_display = "name", "price", "quantity", "description", "image",


admin.site.register(Omegameds,OmegamedsAdmin),
