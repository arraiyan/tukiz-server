# Generated by Django 3.2.3 on 2021-06-24 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_postbody'),
    ]

    operations = [
        migrations.CreateModel(
            name='postfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(default='none.jpg', upload_to='files/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.post')),
            ],
        ),
    ]
