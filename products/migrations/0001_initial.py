# Generated by Django 5.0.3 on 2024-03-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("description_img", models.URLField(default=None, null=True)),
                ("description_text", models.TextField(default=None, null=True)),
                ("price", models.IntegerField()),
                ("sale", models.IntegerField(default=None, null=True)),
                ("view_count", models.IntegerField(default=0)),
                ("status", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
