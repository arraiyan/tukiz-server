# Generated by Django 3.2.3 on 2021-06-24 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_postphotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='postbody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.post')),
            ],
        ),
    ]
