# Generated by Django 2.1.2 on 2018-10-23 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181023_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='dataset',
            field=models.ForeignKey(db_column='dataset', on_delete='models.CASCADE', to='contribute.Dataset', to_field='label'),
        ),
    ]
