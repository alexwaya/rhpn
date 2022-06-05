# Generated by Django 4.0.4 on 2022-06-05 15:04

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_alter_facility_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='location',
            field=mapbox_location_field.models.LocationField(map_attrs={'center': [1.284135, 36.811868], 'marker_color': 'blue', 'style': 'mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72'}),
        ),
    ]