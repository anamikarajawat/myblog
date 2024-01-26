# Generated by Django 5.0.1 on 2024-01-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tittle',
            new_name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(default='default_image.jpg', upload_to='article_image/'),
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]