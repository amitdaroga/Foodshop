# Generated by Django 4.1.5 on 2023-01-21 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_admin', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp_verification',
            name='user',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='OTP_Verification',
        ),
    ]