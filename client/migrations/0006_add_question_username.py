# Generated by Django 4.2 on 2023-04-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_add_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_question',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
