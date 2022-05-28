# Generated by Django 4.0.4 on 2022-05-28 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_merge_20220526_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('display_image', models.ImageField(upload_to='images/course_image/display_images/')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course_head')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faculty')),
            ],
        ),
    ]
