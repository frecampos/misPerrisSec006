# Generated by Django 3.2 on 2021-05-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misPerris', '0005_auto_20210519_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='usuario',
            field=models.CharField(max_length=45, null=True),
        ),
    ]