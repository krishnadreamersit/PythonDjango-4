# Generated by Django 4.0.3 on 2022-04-05 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2_1', '0005_publication_alter_person_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('contents', models.CharField(max_length=500)),
                ('publication', models.ManyToManyField(to='app2_1.publication')),
            ],
        ),
    ]