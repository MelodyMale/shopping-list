# Generated by Django 4.1.5 on 2023-01-05 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(default="New item", max_length=100)),
                ("checked", models.BooleanField(default=False)),
            ],
        ),
    ]
