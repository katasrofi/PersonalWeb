# Generated by Django 4.2 on 2024-10-04 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=555)),
                ('title', models.CharField(max_length=255)),
                ('asin', models.CharField(max_length=100, unique=True)),
                ('price', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=90)),
                ('product_details', models.TextField()),
                ('breadcrumbs', models.CharField(max_length=255)),
                ('images_list', models.JSONField()),
                ('features', models.JSONField()),
            ],
        ),
    ]
