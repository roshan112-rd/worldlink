# Generated by Django 3.2 on 2022-12-11 09:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0018_alter_testimonial_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='star',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
