# Generated by Django 4.0.2 on 2022-07-02 02:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
