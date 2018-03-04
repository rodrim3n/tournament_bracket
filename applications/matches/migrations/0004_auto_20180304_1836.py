# Generated by Django 2.0.2 on 2018-03-04 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_match_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='communities.Community'),
        ),
    ]
