# Generated by Django 3.0.8 on 2020-08-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HackuizCTF', '0012_auto_20200807_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='challenge_score',
            field=models.IntegerField(default=0),
        ),
    ]
