# Generated by Django 3.0.5 on 2020-04-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='sprites_back_default',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sprites_back_female',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sprites_back_shiny',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sprites_back_shiny_female',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sprites_front_default',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sprites_front_female',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sprites_front_shiny',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sprites_front_shiny_female',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
