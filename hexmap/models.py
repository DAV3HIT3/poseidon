from django.db import models

class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    class Meta:
        unique_together = ('x', 'y', 'z')

class RegionType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Hex map tile region
class Region(models.Model):
    coordinate = models.ForeignKey(Point, on_delete=models.CASCADE, null=True)
    region_type = models.ForeignKey(RegionType, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
