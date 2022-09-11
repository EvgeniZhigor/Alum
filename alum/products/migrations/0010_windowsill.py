# Generated by Django 4.0.6 on 2022-09-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Windowsill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Подоконник',
                'verbose_name_plural': 'Подоконники',
            },
        ),
    ]
