# Generated by Django 3.0.8 on 2020-08-07 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HackuizCTF', '0011_auto_20200806_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackuiz_taker',
            name='challenge_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HackuizCTF.Challenges'),
        ),
    ]
