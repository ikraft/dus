from django.contrib import admin
from .models import Analytics

class AnalyticsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Analytics, AnalyticsAdmin)