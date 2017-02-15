# Generated by Django 2.0.dev20170211211108 on 2017-02-15 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_category'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='upvoted',
            field=models.ManyToManyField(blank=True, related_name='upvoters', to='posts.Post'),
        ),
    ]