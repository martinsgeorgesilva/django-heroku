# Generated by Django 3.1.2 on 2021-03-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atelier', '0003_imersion_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imersion',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
