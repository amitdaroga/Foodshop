# Generated by Django 4.1.5 on 2023-01-22 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_admin', '0013_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=200)),
                ('ProductCategory', models.CharField(max_length=200)),
                ('ProductDueDate', models.DateField(max_length=100)),
            ],
        ),
    ]
