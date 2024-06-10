# Generated by Django 5.0.6 on 2024-06-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rgb_value', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Toyota', 'Toyota')], max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('engine_power', models.IntegerField()),
                ('engine_type', models.CharField(choices=[('diesel', 'Diesel'), ('petrol', 'Petrol'), ('electric', 'Electric'), ('hybrid', 'Hybrid')], max_length=50)),
                ('body_type', models.CharField(choices=[('sedan', 'Sedan'), ('hatchback', 'Hatchback'), ('suv', 'SUV'), ('coupe', 'Coupe'), ('kombi', 'Kombi'), ('van', 'Van')], default='', max_length=50)),
                ('door_count', models.IntegerField()),
                ('image', models.ImageField(default='', upload_to='photos/')),
                ('colors', models.ManyToManyField(to='toyotasite.color')),
            ],
        ),
    ]