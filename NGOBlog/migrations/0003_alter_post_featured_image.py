# Generated by Django 3.2 on 2023-02-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGOBlog', '0002_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/featured_image'),
        ),
    ]
