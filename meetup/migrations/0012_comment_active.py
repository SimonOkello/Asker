# Generated by Django 2.2.6 on 2019-11-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0011_auto_20191116_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
