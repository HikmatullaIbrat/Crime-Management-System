# Generated by Django 4.0 on 2022-02-15 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=64)),
                ('village', models.CharField(max_length=64)),
                ('district', models.CharField(max_length=64)),
                ('home_number', models.CharField(max_length=64)),
            ],
        ),
    ]
