from django.conf import settings
from django.db import models

# Atlantis faction 
class Faction(models.Model):
    faction_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name + " (" + str(self.faction_id) + ")"

    class Meta:
        ordering = ('faction_id', 'name',)

# User faction (player), connect faction to user
class UserFaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    war_points = models.IntegerField()
    trade_points = models.IntegerField()
    magic_points = models.IntegerField()

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

# User turn error report
class TurnError(models.Model):
    user_turn = models.ForeignKey(UserTurn, on_delete=models.CASCADE)
    text = models.TextField()

# User turn event
class TurnEvent(models.Model):
    user_turn = models.ForeignKey(UserTurn, on_delete=models.CASCADE)
    text = models.TextField()

# Basic atlantis "unit"
class Unit(models.Model):
    unit_id = models.IntegerField(unique=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    is_mage = models.BooleanField(default=False)
    is_quartermaster = models.BooleanField(default=False)
    purchase_cost = models.IntegerField()
    maintenance_cost = models.IntegerField()

 # Atlantis race
class Race(models.Model):
    name = models.CharField(max_length=120)
    default_max_level = models.IntegerField()

# Atlantis skill 
class Skill(models.Model):
    name = models.CharField(max_length=120)
    shortcut = models.CharField(max_length=20)
    description = models.CharField(max_length=120)

# A unit can contain "groups" of different races
class UnitMember(models.Model):
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

# Unit skill level
class UnitSkill(models.Model):
    unit = models.ForeignKey(UnitMember, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_level = models.IntegerField()

# Race specialized skills
class RaceSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    max_level = models.IntegerField()

# Skill level description
class SkillLevel(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField()
    description = models.CharField(max_length=120)



