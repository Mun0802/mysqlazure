# Generated by Django 4.0.3 on 2022-04-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_doctor_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_site_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='reset_otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='doc_score',
            field=models.BigIntegerField(default=0),
        ),
    ]
