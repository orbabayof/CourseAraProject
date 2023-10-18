# Generated by Django 4.2.6 on 2023-10-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menuapp', '0004_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('age', models.IntegerField(default=5)),
            ],
        ),
    ]