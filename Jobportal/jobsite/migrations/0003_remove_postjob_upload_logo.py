# Generated by Django 4.1.5 on 2023-05-22 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsite', '0002_remove_postjob_description_alter_postjob_upload_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postjob',
            name='Upload_Logo',
        ),
    ]
