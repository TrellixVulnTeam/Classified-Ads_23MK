# Generated by Django 3.0.4 on 2020-04-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0034_auto_20200420_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catugry',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
