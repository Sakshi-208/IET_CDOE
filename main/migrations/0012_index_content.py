# Generated by Django 4.0.4 on 2022-05-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_emailcomingsoon'),
    ]

    operations = [
        migrations.CreateModel(
            name='index_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_header', models.CharField(max_length=200)),
                ('about_head', models.CharField(max_length=200)),
                ('about_body', models.TextField()),
            ],
        ),
    ]
