# Generated by Django 2.2.4 on 2019-08-06 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_com_status',
            new_name='completed',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_desc',
            new_name='title',
        ),
    ]
