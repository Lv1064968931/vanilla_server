# Generated by Django 2.2.2 on 2019-06-30 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phoneverifyrecord',
            old_name='phone_num',
            new_name='phone',
        ),
    ]