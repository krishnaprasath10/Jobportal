# Generated by Django 4.1.5 on 2023-05-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Job_Title', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
                ('Job_Region', models.CharField(max_length=50)),
                ('Job_Type', models.CharField(max_length=50)),
                ('Job_Description', models.CharField(max_length=50)),
                ('Company_Name', models.CharField(max_length=50)),
                ('Company_Description', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
                ('Website', models.CharField(max_length=50)),
                ('Facebook_Username', models.CharField(max_length=50)),
                ('Twitter_Username', models.CharField(max_length=50)),
                ('Linkedin_Username', models.CharField(max_length=50)),
                ('Upload_Logo', models.CharField(max_length=50)),
            ],
        ),
    ]