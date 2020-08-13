from django.contrib import admin

from .models import *

class FactionAdmin(admin.ModelAdmin):
    list_display = ('faction_id', 'name')

class TurnAdmin(admin.ModelAdmin):
    list_display = ('turn_id', 'year', 'month')

class TurnErrorInline(admin.StackedInline):
    model = TurnError

class TurnEventInline(admin.StackedInline):
    model = TurnEvent

class UserTurnAdmin(admin.ModelAdmin):
    inlines = [TurnErrorInline, TurnEventInline]
    list_display = ('turn', 'user_faction')

admin.site.register(Faction, FactionAdmin)
admin.site.register(UserFaction)

admin.site.register(Turn, TurnAdmin)
admin.site.register(TimesArticle)

admin.site.register(UserTurn, UserTurnAdmin)
