# Generated by Django 4.1.3 on 2023-01-02 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='modified_at',
        ),
    ]
