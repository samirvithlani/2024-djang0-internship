# Generated by Django 4.2.9 on 2024-02-05 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]