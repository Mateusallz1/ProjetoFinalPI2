# Generated by Django 3.0 on 2021-01-28 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('trainers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainers_tut', to='pokes.Trainer')),
            ],
        ),
    ]
