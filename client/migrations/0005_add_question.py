# Generated by Django 4.2 on 2023-04-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20230307_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('question_des', models.TextField()),
                ('user_role', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100, null=True)),
                ('user_id', models.CharField(max_length=100, null=True)),
                ('votecount', models.CharField(max_length=100, null=True)),
                ('dislike', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Questions',
                'ordering': ('-question',),
            },
        ),
    ]
