# Generated by Django 5.0.7 on 2024-07-16 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_travelpost_detail_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelpost',
            old_name='cupon',
            new_name='coupon',
        ),
    ]
