# Generated by Django 2.2.12 on 2021-08-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_app', '0003_auto_20210825_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('description', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
