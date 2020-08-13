from django.db import models

# Atlantis faction (player)
class Faction(models.Model):
    faction_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=120)

# Faction details
class FactionDetail(models.Model):
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    password = models.CharField(max_length=120)
    war_points = models.IntegerField()
    trade_points = models.IntegerField()
    magic_points = models.IntegerField()

# Atlantis turn
class Turn(models.Model):
    turn_id = models.IntegerField(unique=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()

# Turn error report
class TurnError(models.Model):
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
    text = models.TextField()

# Turn times article
class TimesArticle(models.Model):
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
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



