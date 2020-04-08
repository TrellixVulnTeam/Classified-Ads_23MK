# Generated by Django 2.1.5 on 2020-04-06 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20200405_0421'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.PositiveSmallIntegerField(choices=[('1', 'Aston Martin'), ('2', 'Audi'), ('3', 'BMW'), ('4', 'Cadillac'), ('5', 'Chevrolet'), ('6', 'Ferrari'), ('7', 'Datsun'), ('8', 'Ford'), ('9', 'Rolls-Royce'), ('10', 'Toyota')])),
                ('general_ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ads')),
            ],
        ),
    ]
