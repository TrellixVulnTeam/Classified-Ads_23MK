# Generated by Django 2.1.5 on 2020-06-17 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0004_auto_20200617_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_details', models.CharField(max_length=120)),
                ('center_city', models.ForeignKey(blank=True, limit_choices_to={'center_city__isnull': True, 'governorate_name__isnull': False, 'region_village__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cho_center_city', to='user_profile.governorate')),
                ('governorate_name', models.ForeignKey(blank=True, limit_choices_to={'center_city__isnull': True, 'governorate_name__isnull': True, 'region_village__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cho_governorate_name', to='user_profile.governorate')),
                ('last', models.ForeignKey(blank=True, limit_choices_to={'center_city__isnull': False, 'governorate_name__isnull': False, 'region_village__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cho_last', to='user_profile.governorate', verbose_name='Last adress')),
                ('region_village', models.ForeignKey(blank=True, limit_choices_to={'center_city__isnull': False, 'governorate_name__isnull': False, 'region_village__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cho_region_village', to='user_profile.governorate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
