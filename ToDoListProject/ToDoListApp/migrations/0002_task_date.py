# Generated by Django 4.1.7 on 2023-02-16 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoListApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-02-23'),
            preserve_default=False,
        ),
    ]
