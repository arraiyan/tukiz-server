# Generated by Django 3.2.3 on 2021-05-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='No title', max_length=250),
        ),
    ]
