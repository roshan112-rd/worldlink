# Generated by Django 3.2 on 2022-12-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0009_alter_slider_custom_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='order',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='tourcategory',
            name='order',
            field=models.IntegerField(default='1'),
        ),
    ]
