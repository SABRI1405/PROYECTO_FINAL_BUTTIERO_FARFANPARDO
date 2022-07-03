# Generated by Django 4.0.4 on 2022-06-23 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Informacion', '0002_archivo_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivo',
            old_name='subtitulo',
            new_name='autor',
        ),
        migrations.RemoveField(
            model_name='archivo',
            name='imagen',
        ),
        migrations.AlterField(
            model_name='archivo',
            name='adjunto',
            field=models.URLField(),
        ),
    ]