# Generated by Django 3.2.4 on 2021-07-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0008_alter_patients_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='maxn',
            field=models.IntegerField(default=50, verbose_name='Макс. число работников'),
        ),
    ]