# Generated by Django 5.0.6 on 2024-08-08 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=20)),
                ('reference_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('reg_number', models.CharField(max_length=20)),
                ('current_year_of_study', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_fees_receipt', models.ImageField(upload_to='receipts/')),
                ('dept_fees_receipt', models.ImageField(upload_to='receipts/')),
                ('faculty_fees_receipt', models.ImageField(upload_to='receipts/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.user')),
            ],
        ),
    ]