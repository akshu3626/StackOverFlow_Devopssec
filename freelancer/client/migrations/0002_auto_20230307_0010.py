# Generated by Django 2.1.15 on 2023-03-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpostmodel',
            name='user_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
