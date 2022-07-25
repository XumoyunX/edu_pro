# Generated by Django 4.0.6 on 2022-07-25 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coueres_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SmallIntegerField(choices=[(1, 'pul'), (2, 'tekin')])),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('job', models.CharField(max_length=250)),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team_bola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=250)),
                ('job', models.TextField()),
                ('instagram', models.CharField(max_length=250)),
                ('github', models.CharField(max_length=250)),
                ('fezbook', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Coueres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('course_data', models.CharField(max_length=250)),
                ('joy_qolgan', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='video/')),
                ('coueres_price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.coueres_price')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
