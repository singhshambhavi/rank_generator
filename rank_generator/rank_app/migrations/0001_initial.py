# Generated by Django 3.1.4 on 2020-12-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uuid', models.IntegerField()),
                ('topic', models.CharField(max_length=1250)),
                ('score', models.IntegerField()),
            ],
            options={
                'db_table': 'details',
            },
        ),
    ]
