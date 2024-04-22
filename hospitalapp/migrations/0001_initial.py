# Generated by Django 5.0.3 on 2024-03-13 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_name', models.CharField(max_length=100)),
                ('Doctor_special', models.CharField(max_length=100)),
                ('Doctor_img', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=10)),
                ('Email_Id', models.EmailField(max_length=254)),
                ('Booking_date', models.DateField()),
                ('Booked_on', models.DateField(auto_now_add=True)),
                ('Doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.doctors')),
            ],
        ),
    ]
