# Generated by Django 5.0.6 on 2024-07-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_travelpost_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelpost',
            name='cupon',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
