# Generated by Django 3.1.2 on 2020-11-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorProducto', '0002_adopcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adopcion',
            name='activo',
        ),
        migrations.AddField(
            model_name='adopcion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='adopta/', verbose_name='Imagen'),
        ),
    ]