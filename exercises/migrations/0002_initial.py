# Generated by Django 4.1.7 on 2023-03-02 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("exercises", "0001_initial"),
        ("training_day", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="training_day",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exercises",
                to="training_day.training_day",
            ),
        ),
    ]
