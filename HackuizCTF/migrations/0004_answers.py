# Generated by Django 3.0.8 on 2020-08-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HackuizCTF', '0003_hackuiz_taker_taker_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crct_ans', models.CharField(max_length=100)),
            ],
        ),
    ]
