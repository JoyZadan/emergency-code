# Generated by Django 3.2 on 2023-02-17 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, max_length=100', max_length=100)),
                ('friendly_name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(help_text='format: max_length=100', max_length=100, unique=True, verbose_name='Category slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NonGovernmentOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, max_length=200', max_length=200)),
                ('slug', models.SlugField(help_text='format: required, max_length=200', max_length=200, unique=True, verbose_name='NGO slug')),
                ('is_featured', models.BooleanField(default=False)),
                ('description', models.TextField(help_text='format: reqd, max_length=2000', max_length=2000)),
                ('website', models.CharField(help_text='format: reqd, max_length=150', max_length=150)),
                ('image_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngos.category')),
            ],
            options={
                'verbose_name': 'NonGovernmentOrganization',
                'verbose_name_plural': 'NGOs',
                'ordering': ['name'],
            },
        ),
    ]
