# Generated by Django 3.1.5 on 2021-07-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]