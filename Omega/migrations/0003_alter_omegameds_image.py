# Generated by Django 5.0.6 on 2024-07-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Omega', '0002_alter_omegameds_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omegameds',
            name='image',
            field=models.CharField(max_length=250),
        ),
    ]
