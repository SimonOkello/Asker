# Generated by Django 2.2.6 on 2019-10-26 04:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]