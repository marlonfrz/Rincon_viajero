# Generated by Django 5.0.7 on 2024-07-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_cupon_travelpost_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelpost',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
