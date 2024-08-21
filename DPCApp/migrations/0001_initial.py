# Generated by Django 5.1 on 2024-08-15 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainSuffix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suffix', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DomainDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domainName', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('domainSuffix', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DPCApp.domainsuffix')),
                ('websiteName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DPCApp.websitename')),
            ],
        ),
    ]
