# Generated by Django 3.2 on 2021-05-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misPerris', '0006_mascota_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(default='mascotas/defecto.jpg', upload_to='mascotas'),
        ),
    ]
