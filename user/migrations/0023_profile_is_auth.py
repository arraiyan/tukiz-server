# Generated by Django 3.2.3 on 2021-07-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_auth',
            field=models.BooleanField(default=False),
        ),
    ]
