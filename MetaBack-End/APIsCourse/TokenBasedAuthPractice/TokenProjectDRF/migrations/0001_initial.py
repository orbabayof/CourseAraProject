# Generated by Django 4.2.7 on 2023-11-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecretMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('contenct', models.TextField(max_length=2000)),
            ],
        ),
    ]
