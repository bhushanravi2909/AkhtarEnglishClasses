# Generated by Django 2.2.5 on 2019-10-13 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=200)),
                ('Posted_date', models.CharField(max_length=10)),
            ],
        ),
    ]
