# Generated by Django 2.2.5 on 2019-10-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchTiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch', models.CharField(max_length=10)),
                ('Timing', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='std_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Father_Name', models.CharField(max_length=20)),
                ('Mother_Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Confirm_Email', models.EmailField(max_length=254)),
                ('Mobile', models.BigIntegerField()),
                ('Address', models.TextField(max_length=40)),
                ('ZipCode', models.IntegerField()),
            ],
        ),
    ]
