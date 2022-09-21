# Generated by Django 4.1.1 on 2022-09-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('path', models.CharField(max_length=250)),
                ('mime_type', models.CharField(max_length=25)),
            ],
        ),
    ]
