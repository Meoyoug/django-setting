# Generated by Django 5.0.3 on 2024-04-03 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_img",
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="sale",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
