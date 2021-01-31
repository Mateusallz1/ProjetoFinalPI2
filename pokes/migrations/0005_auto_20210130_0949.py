# Generated by Django 3.0 on 2021-01-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokes', '0004_auto_20210129_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='trainer',
        ),
        migrations.AddField(
            model_name='trainer',
            name='pokemon',
            field=models.ManyToManyField(related_name='pokemon', to='pokes.Pokemon'),
        ),
    ]