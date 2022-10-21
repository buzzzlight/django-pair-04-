# Generated by Django 3.2.13 on 2022-10-21 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
