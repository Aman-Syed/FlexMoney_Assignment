# Generated by Django 2.1 on 2022-12-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20221212_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('payamount', models.IntegerField()),
                ('batch', models.TextField()),
                ('month', models.TextField()),
                ('year', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('userid', models.IntegerField()),
                ('email', models.TextField()),
                ('phno', models.TextField()),
                ('age', models.IntegerField()),
                ('password', models.TextField()),
            ],
        ),
    ]