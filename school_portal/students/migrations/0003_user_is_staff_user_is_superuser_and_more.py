# Generated by Django 5.0.6 on 2024-08-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_courseregistration_confirmfees'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='matric_number',
            field=models.CharField(default='1234', max_length=20, unique=True),
        ),
    ]
