# Generated by Django 3.1.1 on 2020-11-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20201124_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescuee',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Waiting'), ('Going', 'On The Way')], default='On The Way', max_length=30),
        ),
    ]
