# Generated by Django 2.2.10 on 2020-03-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200313_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default='no description'),
            preserve_default=False,
        ),
    ]
