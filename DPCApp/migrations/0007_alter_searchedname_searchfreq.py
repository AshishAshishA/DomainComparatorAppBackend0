# Generated by Django 5.1 on 2024-08-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DPCApp', '0006_alter_searchedname_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchedname',
            name='searchFreq',
            field=models.IntegerField(default=1),
        ),
    ]
