# Generated by Django 5.0 on 2024-01-02 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter_table',
            name='last_task_id',
            field=models.IntegerField(default=0),
        ),
    ]
