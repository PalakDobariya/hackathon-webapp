# Generated by Django 2.2.6 on 2019-11-11 11:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_auto_20191110_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackathonEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=80)),
                ('event_description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
