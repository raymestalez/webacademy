# Generated by Django 2.0.dev20170211211108 on 2017-02-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('posts', '0002_post_post_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='tags.Tag'),
        ),
    ]
