# Generated by Django 2.2.12 on 2021-08-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]