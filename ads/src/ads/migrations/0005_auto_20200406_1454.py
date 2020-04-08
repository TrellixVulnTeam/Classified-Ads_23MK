# Generated by Django 2.1.5 on 2020-04-06 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_body',
            field=models.PositiveSmallIntegerField(choices=[('1', 'suv'), ('2', 'sedan'), ('3', 'AR-8'), ('4', 'bus'), ('5', 'h-bag'), ('7', 'OTHER')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.PositiveSmallIntegerField(choices=[('1', 'Aston Martin'), ('2', 'Audi'), ('3', 'BMW'), ('4', 'Cadillac'), ('5', 'Chevrolet'), ('6', 'Ferrari'), ('7', 'Datsun'), ('8', 'Ford'), ('9', 'Rolls-Royce'), ('10', 'Toyota')], default=1),
            preserve_default=False,
        ),
    ]
