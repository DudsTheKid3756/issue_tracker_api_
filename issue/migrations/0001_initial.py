# Generated by Django 4.1.7 on 2023-04-09 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('alert', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=28)),
                ('comment', models.TextField(max_length=255)),
                ('color', models.CharField(default='#000000', max_length=7)),
                ('created_by', models.CharField(max_length=15)),
                ('created', models.DateTimeField()),
                ('has_reminder', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('reminder', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='issue.reminder')),
            ],
        ),
    ]
