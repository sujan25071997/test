# Generated by Django 3.0.5 on 2020-12-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_profile',
            name='paid_amount',
            field=models.IntegerField(null=True),
        ),
    ]