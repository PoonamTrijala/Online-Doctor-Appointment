# Generated by Django 3.1.5 on 2021-07-24 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=250)),
                ('full_name', models.CharField(max_length=250)),
                ('phone_number', models.IntegerField(max_length=250)),
                ('message', models.CharField(max_length=250)),
                ('appointment_time', models.TimeField(max_length=12)),
                ('appointment_date', models.DateField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=250)),
                ('cat_img', models.FileField(upload_to='media')),
                ('cat_desc', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=250, null=True)),
                ('symptoms', models.CharField(max_length=250)),
                ('complains', models.CharField(max_length=250)),
                ('bp', models.CharField(max_length=250)),
                ('temperature', models.CharField(max_length=250)),
                ('weight', models.CharField(max_length=250)),
                ('fever', models.CharField(max_length=250)),
                ('pain_condition', models.CharField(max_length=250)),
                ('physical_appearence', models.CharField(max_length=250)),
                ('Deformation', models.CharField(max_length=250)),
                ('appetite', models.CharField(max_length=250)),
                ('sleep_conditions', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('profile', models.ImageField(upload_to='media')),
                ('contact_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250)),
                ('occupation', models.TextField(max_length=250)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('update_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('profile', models.ImageField(upload_to='media')),
                ('contact_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250)),
                ('occupation', models.TextField(max_length=250)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('update_on', models.DateTimeField(auto_now_add=True)),
                ('patient', models.CharField(max_length=250, null=True)),
                ('aap_time', models.CharField(max_length=250, null=True)),
                ('contact', models.CharField(max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='media')),
                ('contact_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250)),
                ('occupation', models.TextField(max_length=250)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('update_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Addpatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=250)),
                ('patient_img', models.ImageField(upload_to='media')),
                ('patient_number', models.IntegerField()),
                ('patient_address', models.CharField(max_length=250)),
                ('patient_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], max_length=250)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]