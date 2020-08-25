from django.db import models

class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    def __str__(self):
        return "(" + str(x) + "," + str(y) + "," + str(z) + ")"

class RegionType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return name

# Hex map tile region
class Region(models.Model):
    coordinate = models.ForeignKey(Point, on_delete=models.CASCADE)
    region_type = models.ForeignKey(RegionType, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return name
