# Generated by Django 3.1.2 on 2020-10-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_remove_projectvehicle_user_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='points',
            name='projectID',
        ),
        migrations.RemoveField(
            model_name='points',
            name='sectionID',
        ),
        migrations.RemoveField(
            model_name='sectionvehicle',
            name='projectID',
        ),
        migrations.AddField(
            model_name='points',
            name='projectlabel',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='points',
            name='sectionlabel',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sectionvehicle',
            name='projectlabel',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
