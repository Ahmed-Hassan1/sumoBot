# Generated by Django 3.2.24 on 2024-03-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0011_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='targetClientId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetClientId2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetClientId3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetClientId4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetClientIdBase',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetOrderId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetOrderId2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetOrderId3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetOrderId4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='targetOrderIdBase',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
