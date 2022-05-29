# Generated by Django 4.0.4 on 2022-05-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_index_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_details',
            name='apply_link',
            field=models.URLField(default='#'),
        ),
        migrations.AddField(
            model_name='course_details',
            name='course_price',
            field=models.CharField(default='Free', max_length=200),
        ),
    ]
