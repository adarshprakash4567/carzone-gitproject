# Generated by Django 3.2.9 on 2022-02-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='no_of_owners',
            field=models.CharField(max_length=50),
        ),
    ]
