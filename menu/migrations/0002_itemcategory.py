# Generated by Django 5.0.1 on 2024-01-21 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100)),
                ('RestaurantID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.restaurant')),
            ],
        ),
    ]
