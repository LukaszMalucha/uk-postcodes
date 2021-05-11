# Generated by Django 2.2 on 2021-05-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostcodeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(max_length=254, unique=True)),
                ('lat', models.CharField(max_length=254, unique=True)),
                ('long', models.CharField(max_length=254, unique=True)),
                ('county', models.CharField(blank=True, max_length=254)),
                ('district', models.CharField(blank=True, max_length=254)),
                ('ward', models.CharField(blank=True, max_length=254)),
                ('constituency', models.CharField(blank=True, max_length=254)),
            ],
        ),
    ]