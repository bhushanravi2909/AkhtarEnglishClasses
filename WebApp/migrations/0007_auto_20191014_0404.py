# Generated by Django 2.2.5 on 2019-10-13 22:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_auto_20191014_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='Posted_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='SubDate',
            field=models.DateField(),
        ),
    ]
