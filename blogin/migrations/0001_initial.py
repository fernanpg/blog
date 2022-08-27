# Generated by Django 2.2 on 2022-08-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('body', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
