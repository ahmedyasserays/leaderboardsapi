# Generated by Django 3.2.4 on 2021-06-24 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renderer', '0002_auto_20210624_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='leader_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renderer.leaderboard'),
        ),
    ]
