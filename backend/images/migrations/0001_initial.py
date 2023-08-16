# Generated by Django 4.2.4 on 2023-08-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=10)),
                ('image_base64', models.TextField()),
            ],
        ),
    ]
