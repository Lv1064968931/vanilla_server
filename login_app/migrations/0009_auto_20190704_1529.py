# Generated by Django 2.2.2 on 2019-07-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0008_auto_20190704_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='book_plan_count',
            field=models.CharField(default='18', max_length=11, verbose_name='计划数'),
        ),
    ]