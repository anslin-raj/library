# Generated by Django 3.2.2 on 2022-09-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_auto_20220913_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.CharField(max_length=255),
        ),
    ]