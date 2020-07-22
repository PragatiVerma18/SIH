# Generated by Django 3.0.8 on 2020-07-22 16:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20200722_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('last_date', models.DateTimeField()),
                ('company_name', models.CharField(max_length=100)),
                ('vacancies', models.IntegerField(default=1)),
                ('doc_url', models.URLField(blank=True)),
                ('summary', models.CharField(blank=True, max_length=500)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('filled', models.BooleanField(default=False)),
                ('salary', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User', to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='jobs.Job')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.User', to_field='username')),
            ],
        ),
    ]
