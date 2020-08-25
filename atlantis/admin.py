from django.contrib import admin

from .models import *

class FactionAdmin(admin.ModelAdmin):
    list_display = ('faction_id', 'name')

class TurnAdmin(admin.ModelAdmin):
    list_display = ('turn_number', 'year', 'month')

class TurnErrorInline(admin.StackedInline):
    model = TurnError
    extra = 0

class TurnEventInline(admin.StackedInline):
    model = TurnEvent
    extra = 0

class UserTurnAdmin(admin.ModelAdmin):
    inlines = [TurnErrorInline, TurnEventInline]
    list_display = ('turn', 'user_faction')

class UnitDetailInline(admin.StackedInline):
    model = UnitDetail
    extra = 0

class TurnErrorInline(admin.StackedInline):
    model = TurnError
    extra = 0

class TurnEventInline(admin.StackedInline):
    model = TurnEvent
    extra = 0

class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_id',)
    inlines = [UnitDetailInline,TurnErrorInline,TurnEventInline]

# Faction
admin.site.register(Faction, FactionAdmin)

# UserFaction
admin.site.register(UserFaction)

# Attitude
admin.site.register(Attitude)

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

# Turn errors
admin.site.register(TurnError)

# Turn events
admin.site.register(TurnEvent)

class SkillLevelInline(admin.StackedInline):
    model = SkillLevel
    extra = 0

class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillLevelInline, ]

# Skills
admin.site.register(Skill, SkillAdmin)


# Unit
admin.site.register(Unit, UnitAdmin)


