# Generated by Django 2.1.2 on 2018-12-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='employment',
            field=models.CharField(choices=[('TA', 'Teaching Assistant'), ('ST', 'Student'), ('PR', 'Junior')], default='ST', max_length=2),
        ),
    ]
