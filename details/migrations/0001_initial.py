# Generated by Django 3.2.4 on 2021-06-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('food_pic', models.ImageField(upload_to='media')),
                ('vendor_name', models.CharField(max_length=50)),
                ('specality', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('address1', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=20)),
                ('phoneno', models.CharField(max_length=10)),
            ],
        ),
    ]