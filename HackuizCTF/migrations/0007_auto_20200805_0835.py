# Generated by Django 3.0.8 on 2020-08-05 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HackuizCTF', '0006_auto_20200805_0824'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Challenge_ans',
            new_name='Answers',
        ),
    ]