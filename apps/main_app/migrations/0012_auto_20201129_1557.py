# Generated by Django 3.1.1 on 2020-11-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20201129_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescuee',
            name='status',
            field=models.CharField(blank=True, choices=[('Waiting', 'Waiting for Rescuers'), ('Going', 'Rescuers on the Way')], default='Waiting', max_length=30),
        ),
    ]
