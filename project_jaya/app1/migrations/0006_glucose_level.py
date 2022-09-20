# Generated by Django 4.1.1 on 2022-09-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_psqi_timing_alter_eat_places_daily_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glucose_level',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('Glucose', models.CharField(choices=[('Breakfast', (('Pre', 'Pre'), ('Post', 'Post'))), ('Lunch', (('Pre', 'Post'), ('Pre', 'Post'))), ('Dinner', (('Pre', 'Post'), ('Pre', 'Post')))], max_length=2000)),
            ],
        ),
    ]
