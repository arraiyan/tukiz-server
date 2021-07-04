# Generated by Django 3.2.3 on 2021-05-30 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.FileField(blank=True, default='media/none.jpg', upload_to=''),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('file', models.FileField(blank=True, default='media/none.jpg', upload_to='')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.post')),
            ],
        ),
    ]
