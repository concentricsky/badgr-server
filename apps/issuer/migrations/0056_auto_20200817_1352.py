# Generated by Django 2.2.14 on 2020-08-17 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0055_auto_20200817_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='badgeclass',
            name='image_hash',
            field=models.CharField(blank=True, default='', max_length=72),
        ),
    ]
