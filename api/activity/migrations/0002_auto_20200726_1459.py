# Generated by Django 2.2.6 on 2020-07-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='expected_completion_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
