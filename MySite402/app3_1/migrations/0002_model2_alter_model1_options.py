# Generated by Django 4.0.3 on 2022-04-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('nid', models.IntegerField(help_text='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='TITLE', max_length=100)),
                ('content', models.CharField(help_text='CONTENTS', max_length=5000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='model1',
            options={'ordering': ['id']},
        ),
    ]
