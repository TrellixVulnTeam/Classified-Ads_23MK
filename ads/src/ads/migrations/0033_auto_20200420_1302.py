# Generated by Django 3.0.4 on 2020-04-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0032_auto_20200420_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_rent',
            name='color',
            field=models.CharField(blank=True, choices=[('1', 'Red'), ('2', 'White '), ('3', 'Silver '), ('4', 'Black '), ('5', 'Dark Blue'), ('6', 'Dark Gray'), ('7', 'Dark Green'), ('8', 'Light Brown'), ('9', 'Gold '), ('10', 'Bright Red')], max_length=2, null=True),
        ),
    ]
