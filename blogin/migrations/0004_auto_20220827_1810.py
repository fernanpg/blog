# Generated by Django 2.2 on 2022-08-27 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogin', '0003_auto_20220827_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='header_image',
        ),
    ]
