# Generated by Django 4.0.3 on 2022-04-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=50)),
                ('contactAddress', models.CharField(max_length=50)),
            ],
        ),
    ]
