# Generated by Django 3.2.24 on 2024-03-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0009_auto_20240303_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='clientOrderId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='clientOrderId2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='clientOrderId3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='clientOrderId4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='orderId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='orderId2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='orderId3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entries',
            name='orderId4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
