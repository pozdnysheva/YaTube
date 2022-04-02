# Generated by Django 2.2.16 on 2022-03-31 04:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
