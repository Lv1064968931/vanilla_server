# Generated by Django 2.2.2 on 2019-07-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_vocabulary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senten', models.TextField(max_length=1000, verbose_name='名句')),
            ],
            options={
                'verbose_name': '名句',
                'verbose_name_plural': '名句',
            },
        ),
        migrations.AlterModelOptions(
            name='vocabulary',
            options={'verbose_name': '词汇', 'verbose_name_plural': '词汇'},
        ),
    ]
