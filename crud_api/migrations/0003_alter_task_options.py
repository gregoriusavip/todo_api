# Generated by Django 4.2.3 on 2023-07-24 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_api', '0002_alter_task_due_date_alter_task_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['date_created']},
        ),
    ]
