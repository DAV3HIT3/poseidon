from django.contrib import admin

from .models import *

admin.site.register(Faction)
admin.site.register(UserFaction)

admin.site.register(Turn)
admin.site.register(TimesArticle)

class TurnErrorInline(admin.StackedInline):
    model = TurnError

class TurnEventInline(admin.StackedInline):
    model = TurnEvent

class UserTurnAdmin(admin.ModelAdmin):
    inlines = [TurnErrorInline, TurnEventInline]

admin.site.register(UserTurn, UserTurnAdmin)
