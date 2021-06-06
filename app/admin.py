from django.contrib import admin
from .models import Flexi

class FlexiAdmin(admin.ModelAdmin):
    ordering = ['-id']

admin.site.register(Flexi, FlexiAdmin)
