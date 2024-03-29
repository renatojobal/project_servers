# Generated by Django 4.0.1 on 2022-01-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='url',
        ),
        migrations.AddField(
            model_name='resource',
            name='document',
            field=models.FileField(blank=True, upload_to='media/documents'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='video',
            field=models.FileField(blank=True, upload_to='media/videos'),
        ),
    ]
