# Generated by Django 4.1.5 on 2023-02-12 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kaimyon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kanjitagrelation',
            name='kanji',
        ),
        migrations.RemoveField(
            model_name='kanjitagrelation',
            name='tag',
        ),
        migrations.DeleteModel(
            name='IdiomTagRelation',
        ),
        migrations.DeleteModel(
            name='KanjiTagRelation',
        ),
    ]
