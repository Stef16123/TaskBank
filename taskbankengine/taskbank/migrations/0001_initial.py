# Generated by Django 3.0.4 on 2020-03-22 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('body', models.TextField(blank=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
