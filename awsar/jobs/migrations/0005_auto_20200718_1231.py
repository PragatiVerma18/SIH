# Generated by Django 3.0.8 on 2020-07-18 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200718_0917'),
        ('jobs', '0004_auto_20200718_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]