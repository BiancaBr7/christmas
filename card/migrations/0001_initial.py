# Generated by Django 4.2.1 on 2023-12-16 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
