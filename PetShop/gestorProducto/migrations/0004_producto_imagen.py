# Generated by Django 3.1.2 on 2020-11-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorProducto', '0003_auto_20201110_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='producto/', verbose_name='Foto'),
        ),
    ]
