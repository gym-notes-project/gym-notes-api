from django.db import models

class Serie(models.Model):
    class Meta:
        ordering = ("id",)

    name = models.CharField(max_length=50)
    weigth = models.FloatField()
    reps = models.PositiveSmallIntegerField()
    
    exercise = models.ForeignKey(
        "exercises.Exercise",
        on_delete=models.CASCADE,
        related_name="series",
    )
