# Generated by Django 3.0.8 on 2020-08-05 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HackuizCTF', '0004_answers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Solutions',
        ),
    ]