# Generated by Django 3.2.9 on 2022-04-12 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0002_rename_accessories_accessorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessorie',
            name='category',
            field=models.CharField(choices=[('W', 'Wheel'), ('B', 'Body'), ('S', 'Shock')], max_length=2),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accessories', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accessories.accessorie')),
            ],
        ),
    ]
