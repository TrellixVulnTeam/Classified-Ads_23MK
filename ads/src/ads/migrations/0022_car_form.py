# Generated by Django 3.0.4 on 2020-04-20 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0021_auto_20200417_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='car_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ads')),
            ],
        ),
    ]
