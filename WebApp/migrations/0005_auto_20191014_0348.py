# Generated by Django 2.2.5 on 2019-10-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_auto_20191014_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='Posted_date',
            field=models.DateTimeField(),
        ),
    ]
