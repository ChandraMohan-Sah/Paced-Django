# Generated by Django 5.1.3 on 2024-11-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4_file_uploads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_upload', models.ImageField(upload_to='image_upload')),
            ],
        ),
    ]