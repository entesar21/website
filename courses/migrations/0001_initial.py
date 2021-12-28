# Generated by Django 4.0 on 2021-12-26 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=120)),
                ('course_description', models.TextField()),
                ('course_info', models.TextField()),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='store_image/')),
                ('course_price', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]