# Generated by Django 3.1.2 on 2021-03-15 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0002_auto_20210314_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='imersion',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
