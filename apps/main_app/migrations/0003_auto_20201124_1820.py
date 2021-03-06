# Generated by Django 3.1.1 on 2020-11-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201123_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescuee',
            name='disaster',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rescuee',
            name='children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rescuee',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rescuee',
            name='senior',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rescuee',
            name='total',
            field=models.IntegerField(),
        ),
    ]
