# Generated by Django 4.2.1 on 2023-05-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='title',
            field=models.CharField(default='cda', max_length=255, verbose_name='Тема: '),
        ),
    ]