# Generated by Django 3.1.7 on 2021-03-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssylumHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('services', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('tag', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discription', models.TextField()),
            ],
        ),
    ]