# Generated by Django 3.0.4 on 2020-04-24 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0037_auto_20200420_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='end',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': True, 'main__isnull': False, 'sub__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_end', to='ads.catugry', verbose_name='Deep Category'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='img',
            field=models.ImageField(default='img/defu.png', upload_to='post_img2/'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='last',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': False, 'main__isnull': False, 'sub__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_last', to='ads.catugry', verbose_name='Last Category'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='main',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': True, 'main__isnull': True, 'sub__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_main', to='ads.catugry', verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='sub',
            field=models.ForeignKey(blank=True, limit_choices_to={'end__isnull': True, 'main__isnull': False, 'sub__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_sub', to='ads.catugry', verbose_name='Under Surface Category'),
        ),
    ]
