# Generated by Django 4.0.1 on 2022-03-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0009_job_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
