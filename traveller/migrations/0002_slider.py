# Generated by Django 3.2 on 2022-12-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.TextField()),
                ('image', models.ImageField(upload_to='slider_images')),
                ('text_1', models.TextField()),
                ('text_2', models.TextField()),
                ('text_3', models.TextField()),
                ('text_4', models.TextField()),
                ('custom_link', models.URLField()),
            ],
            options={
                'verbose_name_plural': ' Slider',
            },
        ),
    ]