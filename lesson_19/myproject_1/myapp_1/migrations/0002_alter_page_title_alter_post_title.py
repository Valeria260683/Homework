# Generated by Django 4.2.3 on 2023-07-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
