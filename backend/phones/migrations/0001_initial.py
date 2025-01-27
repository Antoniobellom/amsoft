# Generated by Django 5.0.4 on 2024-07-31 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
                ("year", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.IntegerField()),
            ],
        ),
    ]
