# Generated by Django 2.1.2 on 2018-12-24 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181224_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placegeom',
            name='geom_src',
            field=models.ForeignKey(db_column='geom_src', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Source', to_field='src_id'),
        ),
    ]