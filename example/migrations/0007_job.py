# Generated by Django 4.0.1 on 2022-03-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0006_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
