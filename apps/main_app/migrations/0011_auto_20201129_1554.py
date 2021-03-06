# Generated by Django 3.1.1 on 2020-11-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20201129_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescuee',
            name='status',
            field=models.CharField(blank=True, choices=[('Waiting for Rescuers', 'Waiting'), ('Rescuers on the Way', 'Going')], default='Waiting for Rescuers', max_length=30),
        ),
    ]
