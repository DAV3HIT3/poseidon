from django.conf import settings
from django.db import models

from hexmap.models import *

# Atlantis faction 
class Faction(models.Model):
    faction_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name + " (" + str(self.faction_id) + ")"

    class Meta:
        ordering = ('faction_id', 'name',)

class Attitude(models.Model):
    name = models.CharField(max_length=120)

# User faction (player), connect faction to user
class UserFaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    war_points = models.IntegerField()
    trade_points = models.IntegerField()
    magic_points = models.IntegerField()
    default_attitude = models.ForeignKey(Attitude, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " :  " +  str(self.faction)


# Atlantis turn
class Turn(models.Model):
    turn_id = models.IntegerField(unique=True)
    year = models.IntegerField()
    month = models.IntegerField()

    def __str__(self):
        return str(self.turn_id) + " :  " +  str(self.year) + "/" + str(self.month)

# Turn times article
class TimesArticle(models.Model):
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return str(self.turn) + " : " + str(self.faction)

class UserTurn(models.Model):
    user_faction = models.ForeignKey(UserFaction, on_delete=models.CASCADE)
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
    unclaimed_silver = models.IntegerField()

class FactionAttitude(models.Model):
    user_turn = models.ForeignKey(UserTurn, on_delete=models.CASCADE)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)

# User turn error report
class TurnError(models.Model):
    user_turn = models.ForeignKey(UserTurn, on_delete=models.CASCADE)
    text = models.TextField()

# User turn event
class TurnEvent(models.Model):
    user_turn = models.ForeignKey(UserTurn, on_delete=models.CASCADE)
    text = models.TextField()

 # Atlantis race
class Race(models.Model):
    name = models.CharField(max_length=120)
    default_max_level = models.IntegerField()

 # Atlantis flags
class Flag(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)

# Atlantis skill 
class Skill(models.Model):
    name = models.CharField(max_length=120)
    shortcut = models.CharField(max_length=20)
    description = models.CharField(max_length=120)

# Skill level description
class SkillLevel(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField()
    description = models.CharField(max_length=120)


 # Atlantis items
class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    required_skill = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)

# Basic atlantis "unit"
class Unit(models.Model):
    unit_id = models.IntegerField(unique=True)

class UnitDetail(models.Model):
    user_turn = models.ForeignKey(UserTurn, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    description = models.CharField(max_length=120)
    is_mage = models.BooleanField(default=False)
    is_quartermaster = models.BooleanField(default=False)

# A unit can contain "groups" of different races
class UnitMember(models.Model):
    quantity = models.IntegerField()
    unit = models.ForeignKey(UnitDetail, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    purchase_cost = models.IntegerField()
    maintenance_cost = models.IntegerField()


# Unit skill level
class UnitSkill(models.Model):
    unit = models.ForeignKey(UnitDetail, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_level = models.IntegerField()

class UnitFlag(models.Model):
    unit = models.ForeignKey(UnitDetail, on_delete=models.CASCADE)
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)

class UnitItem(models.Model):
    unit = models.ForeignKey(UnitDetail, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

# Race specialized skills
class RaceSkill(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    skill_level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)



