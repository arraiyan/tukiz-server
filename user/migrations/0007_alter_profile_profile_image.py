# Generated by Django 3.2.3 on 2021-05-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_profile_imagae_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.FileField(default='media/none.jpg', upload_to='profile/'),
        ),
    ]
