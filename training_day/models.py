from django.db import models


class Training_day(models.Model):
    class Meta:
        ordering = ("id",)

    date = models.DateField()
    name = models.CharField(max_length=50)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="training_days",
    )
