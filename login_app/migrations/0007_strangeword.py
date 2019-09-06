# Generated by Django 2.2.2 on 2019-07-03 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strangeword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.CharField(max_length=11, verbose_name='手机号')),
                ('word', models.CharField(max_length=255, verbose_name='单词')),
                ('word_alphabet', models.CharField(max_length=255, verbose_name='音标')),
                ('word_exp', models.CharField(max_length=255, verbose_name='释义')),
            ],
            options={
                'verbose_name': '生词本',
                'verbose_name_plural': '生词本',
            },
        ),
    ]