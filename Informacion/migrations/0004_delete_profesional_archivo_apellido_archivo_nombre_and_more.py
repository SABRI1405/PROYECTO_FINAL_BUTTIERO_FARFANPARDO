# Generated by Django 4.0.4 on 2022-06-25 21:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Informacion', '0003_rename_subtitulo_archivo_autor_remove_archivo_imagen_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profesional',
        ),
        migrations.AddField(
            model_name='archivo',
            name='apellido',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='archivo',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='archivo',
            name='profesion',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
