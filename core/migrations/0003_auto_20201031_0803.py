# Generated by Django 3.0.8 on 2020-10-31 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201029_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='singh', max_length=70),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='singh', max_length=70),
        ),
    ]
