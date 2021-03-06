# Generated by Django 3.0.8 on 2020-08-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpage_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='image',
            field=models.ImageField(default='/static/assets/img/article-1.jpg', upload_to='', verbose_name='title_image'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='quote',
            field=models.CharField(default='', max_length=250),
        ),
    ]
