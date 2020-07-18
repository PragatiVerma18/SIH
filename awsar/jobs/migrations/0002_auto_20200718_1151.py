# Generated by Django 3.0.8 on 2020-07-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='doc_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
