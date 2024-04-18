# Generated by Django 5.0.4 on 2024-04-04 06:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Davlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Positsiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('turi', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='clublar/')),
                ('preidentlar', models.CharField(max_length=255)),
                ('trener', models.CharField(max_length=256)),
                ('t_sana', models.DateField(blank=True, null=True)),
                ('kapital', models.PositiveIntegerField(blank=True, null=True)),
                ('davlat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.davlat')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=60)),
                ('raqam', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('t_sana', models.DateField(blank=True, null=True)),
                ('moash', models.PositiveIntegerField(blank=True, null=True)),
                ('narx', models.PositiveIntegerField()),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.club')),
                ('davlat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.davlat')),
                ('pozitsiya', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.positsiya')),
            ],
        ),
    ]
