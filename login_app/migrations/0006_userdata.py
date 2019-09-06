# Generated by Django 2.2.2 on 2019-07-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0005_sentence_imag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('phone_num', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='手机号')),
                ('book_plan_title', models.CharField(max_length=255, verbose_name='单词书')),
                ('book_plan_count', models.CharField(max_length=11, verbose_name='计划数')),
                ('clock_day_count', models.CharField(max_length=11, verbose_name='打卡天数')),
            ],
            options={
                'verbose_name': '用户数据',
                'verbose_name_plural': '用户数据',
            },
        ),
    ]
