# Generated by Django 4.2.11 on 2024-03-21 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to='gallery')),
                ('thumbnail_path', models.ImageField(upload_to='thumbnails')),
                ('delete_flag', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Uploaded Images',
            },
        ),
    ]
