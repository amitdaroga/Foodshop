# Generated by Django 4.1.5 on 2023-01-21 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_admin', '0003_otp_verification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OTP_Verification',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]