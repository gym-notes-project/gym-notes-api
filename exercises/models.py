from django.db import models

class Exercise(models.Model):
    class Meta:
        ordering = ("id",)

    name = models.CharField(max_length=50)
    training_day = models.ForeignKey(
        "training_day.Training_day",
        on_delete=models.CASCADE,
        related_name="exercises",
        null=False,
    )
