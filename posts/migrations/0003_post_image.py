# Generated by Django 5.0 on 2023-12-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=2, upload_to='posts'),
            preserve_default=False,
        ),
    ]