# Generated by Django 4.2.4 on 2023-08-13 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractSign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('file', models.FileField(upload_to='')),
                ('scanned_file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
