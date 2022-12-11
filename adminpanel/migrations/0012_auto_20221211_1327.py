# Generated by Django 3.2 on 2022-12-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0011_auto_20221211_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='destination_images')),
            ],
        ),
        migrations.DeleteModel(
            name='TourLocation',
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_location',
            field=models.ManyToManyField(to='adminpanel.Destination'),
        ),
    ]