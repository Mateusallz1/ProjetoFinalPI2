# Generated by Django 3.0 on 2021-01-30 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokes', '0006_auto_20210130_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pokemonowner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainer',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='trainers', to=settings.AUTH_USER_MODEL),
        ),
    ]
