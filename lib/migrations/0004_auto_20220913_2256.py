# Generated by Django 3.2.2 on 2022-09-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_alter_book_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
