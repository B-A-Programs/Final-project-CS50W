# Generated by Django 4.0.4 on 2022-06-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobFinderApp', '0008_user_is_company_user_link_to_location_user_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=650)),
                ('requirements', models.CharField(max_length=500)),
            ],
        ),
    ]
