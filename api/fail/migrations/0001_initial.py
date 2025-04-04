# Generated by Django 2.2.6 on 2020-07-26 14:41

import core.helpers
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='NA', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.helpers.PathAndRename('images'))),
                ('document', models.ImageField(blank=True, null=True, upload_to=core.helpers.PathAndRename('document'))),
                ('project_id', models.CharField(default='NA', max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
