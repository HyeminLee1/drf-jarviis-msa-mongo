# Generated by Django 3.0.5 on 2021-12-03 02:43

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('event_id', models.IntegerField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('classification', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('start', models.CharField(blank=True, max_length=25)),
                ('end', models.CharField(blank=True, max_length=25)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.User')),
            ],
            options={
                'db_table': 'events',
            },
        ),
    ]
