# Generated by Django 4.0.2 on 2022-06-25 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.TextField(max_length=200)),
                ('goal', models.IntegerField()),
                ('image', models.URLField()),
                ('date_due', models.DateTimeField()),
                ('is_open', models.BooleanField()),
                ('date_created', models.DateTimeField()),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
    ]
