# Generated by Django 3.0.4 on 2020-04-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0033_auto_20200420_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_form',
            name='Kilometers',
            field=models.CharField(blank=True, choices=[('1', '0 - 999'), ('2', '1000 - 29999 '), ('3', '30000 - 49999'), ('4', '50000 - 99999'), ('5', '100000 - 149999'), ('5', '150000 - 199999'), ('6', 'More Than 200000')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_form',
            name='body_type',
            field=models.CharField(blank=True, choices=[('1', 'SUV'), ('2', 'Sedan'), ('3', 'Cabriolet'), ('4', 'coupe'), ('5', 'Hatchback'), ('6', 'Pickup'), ('7', 'Bus'), ('8', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_form',
            name='color',
            field=models.CharField(blank=True, choices=[('1', 'Red'), ('2', 'White '), ('3', 'Silver '), ('4', 'Black '), ('5', 'Dark Blue'), ('6', 'Dark Gray'), ('7', 'Dark Green'), ('8', 'Light Brown'), ('9', 'Gold '), ('10', 'Bright Red')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='car_form',
            name='engine_capacity',
            field=models.CharField(blank=True, choices=[('1', '0 - 800'), ('2', '1000 - 1300 '), ('3', '1400 - 1600'), ('4', '1800 - 2000'), ('5', '2200 - 2800'), ('6', 'More Than 3000')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_form',
            name='payment_option',
            field=models.CharField(blank=True, choices=[('1', 'Cash'), ('2', 'Exchange'), ('3', 'Installments')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_form',
            name='transmission_type',
            field=models.CharField(blank=True, choices=[('1', 'Automatic'), ('2', 'Manual')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_form',
            name='year',
            field=models.CharField(blank=True, choices=[('1', '2001'), ('2', '2002'), ('3', '2003'), ('4', '2004'), ('5', '2005'), ('6', '2006'), ('7', '2007'), ('8', '2008'), ('9', '2009'), ('10', '2010'), ('11', '2011'), ('12', '2012'), ('13', '2013'), ('14', '2014'), ('15', '2015'), ('16', '2016'), ('17', '2017'), ('18', '2018'), ('19', '2019'), ('20', '2020')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='car_rent',
            name='body_type',
            field=models.CharField(blank=True, choices=[('1', 'SUV'), ('2', 'Sedan'), ('3', 'Cabriolet'), ('4', 'coupe'), ('5', 'Hatchback'), ('6', 'Pickup'), ('7', 'Bus'), ('8', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_rent',
            name='engine_capacity',
            field=models.CharField(blank=True, choices=[('1', '0 - 800'), ('2', '1000 - 1300 '), ('3', '1400 - 1600'), ('4', '1800 - 2000'), ('5', '2200 - 2800'), ('6', 'More Than 3000')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_rent',
            name='rent_duration',
            field=models.CharField(blank=True, choices=[('1', 'Daily'), ('2', 'Monthly'), ('3', 'Yearly')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_rent',
            name='rent_option',
            field=models.CharField(blank=True, choices=[('1', 'With Driver'), ('2', 'Without Driver'), ('3', 'Both Options')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_rent',
            name='transmission_type',
            field=models.CharField(blank=True, choices=[('1', 'Automatic'), ('2', 'Manual')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='car_rent',
            name='year',
            field=models.CharField(blank=True, choices=[('1', '2001'), ('2', '2002'), ('3', '2003'), ('4', '2004'), ('5', '2005'), ('6', '2006'), ('7', '2007'), ('8', '2008'), ('9', '2009'), ('10', '2010'), ('11', '2011'), ('12', '2012'), ('13', '2013'), ('14', '2014'), ('15', '2015'), ('16', '2016'), ('17', '2017'), ('18', '2018'), ('19', '2019'), ('20', '2020')], max_length=2, null=True),
        ),
    ]
