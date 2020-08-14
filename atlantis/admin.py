from django.contrib import admin

from .models import *

class FactionAdmin(admin.ModelAdmin):
    list_display = ('faction_id', 'name')

class TurnAdmin(admin.ModelAdmin):
    list_display = ('turn_id', 'year', 'month')

class TurnErrorInline(admin.StackedInline):
    model = TurnError
    extra = 0

class TurnEventInline(admin.StackedInline):
    model = TurnEvent
    extra = 0

class UserTurnAdmin(admin.ModelAdmin):
    inlines = [TurnErrorInline, TurnEventInline]
    list_display = ('turn', 'user_faction')

# Faction
admin.site.register(Faction, FactionAdmin)

# UserFaction
admin.site.register(UserFaction)

# Turn
admin.site.register(Turn, TurnAdmin)

# Times
admin.site.register(TimesArticle)

# UserTurn
admin.site.register(UserTurn, UserTurnAdmin)

# Races
admin.site.register(Race)

# Flags
admin.site.register(Flag)

class SkillLevelInline(admin.StackedInline):
    model = SkillLevel
    extra = 0

class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillLevelInline, ]

# Skills
admin.site.register(Skill, SkillAdmin)




