# Generated by Django 5.0.5 on 2024-05-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]