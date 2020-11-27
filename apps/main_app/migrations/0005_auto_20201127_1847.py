# Generated by Django 3.1.3 on 2020-11-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rescuee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescuee',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Waiting for Rescuers'), ('Going', 'Rescuers on the Way')], default='Waiting', max_length=30),
        ),
    ]
