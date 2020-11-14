# Generated by Django 3.1.2 on 2020-10-25 21:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('orders_open', models.DateTimeField(default=django.utils.timezone.now)),
                ('orders_close', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProduceBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('orders_open', models.DateTimeField(default=django.utils.timezone.now)),
                ('orders_close', models.DateTimeField(blank=True, null=True)),
                ('season', models.CharField(choices=[('Sp', 'Spring'), ('Fa', 'Fall')], max_length=2)),
                ('contents', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Produce boxes',
            },
        ),
        migrations.CreateModel(
            name='SnackBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('orders_open', models.DateTimeField(default=django.utils.timezone.now)),
                ('orders_close', models.DateTimeField(blank=True, null=True)),
                ('season', models.CharField(choices=[('Sp', 'Spring'), ('Fa', 'Fall')], max_length=2)),
                ('contents', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Snack boxes',
            },
        ),
    ]
