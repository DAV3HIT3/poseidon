from django.contrib import admin

from .models import *

class RegionTypeInline(admin.StackedInline):
    model = RegionType
    extra = 0

class PointInline(admin.StackedInline):
    model = Point
    extra = 0

class RegionAdmin(admin.ModelAdmin):
    inlines = [RegionTypeInline,PointInline]

admin.site.register(Region)
admin.site.register(RegionType)
admin.site.register(Point)
