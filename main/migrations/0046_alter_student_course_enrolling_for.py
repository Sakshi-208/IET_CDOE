# Generated by Django 4.0.4 on 2022-06-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_merge_20220624_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_enrolling_for',
            field=models.CharField(max_length=200),
        ),
    ]
