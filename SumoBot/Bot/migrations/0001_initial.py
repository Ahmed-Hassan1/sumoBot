# Generated by Django 3.2.24 on 2024-02-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.FloatField(blank=True, null=True)),
                ('target', models.FloatField(blank=True, null=True)),
                ('stop', models.FloatField(blank=True, null=True)),
                ('newEntry', models.FloatField(blank=True, null=True)),
                ('newTarget', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
