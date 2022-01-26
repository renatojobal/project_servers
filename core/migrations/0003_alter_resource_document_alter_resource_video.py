# Generated by Django 4.0.1 on 2022-01-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_resource_url_resource_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='document',
            field=models.FileField(blank=True, max_length=255, upload_to='media/documents'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='video',
            field=models.FileField(blank=True, max_length=255, upload_to='media/videos'),
        ),
    ]
