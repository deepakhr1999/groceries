# Generated by Django 2.1.2 on 2018-12-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hostel_name',
            field=models.CharField(default='Old Hostel', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='hostel_number',
            field=models.IntegerField(default=1),
        ),
    ]
