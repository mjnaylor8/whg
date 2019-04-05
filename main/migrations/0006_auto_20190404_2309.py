# Generated by Django 2.1.7 on 2019-04-04 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        ('main', '0005_auto_20190404_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='whg_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='place_id',
            field=models.ForeignKey(default=81525, on_delete=django.db.models.deletion.CASCADE, to='places.Place'),
            preserve_default=False,
        ),
    ]