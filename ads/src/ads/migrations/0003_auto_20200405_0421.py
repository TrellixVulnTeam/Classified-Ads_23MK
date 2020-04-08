# Generated by Django 2.1.5 on 2020-04-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ads_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='adress',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='email',
            field=models.EmailField(blank=True, default='ahmed_mag22@yahoo.com', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='mobile',
            field=models.PositiveSmallIntegerField(blank=True, default=1114796307, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='name_of_who',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
