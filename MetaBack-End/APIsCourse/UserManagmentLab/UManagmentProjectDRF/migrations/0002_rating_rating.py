# Generated by Django 4.2.7 on 2023-11-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UManagmentProjectDRF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]