# Generated by Django 4.1.5 on 2023-01-21 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_admin', '0011_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='All_User',
        ),
        migrations.DeleteModel(
            name='Verification',
        ),
    ]
