# Generated by Django 3.1 on 2021-01-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255, null=True)),
                ('msg', models.CharField(max_length=255, null=True)),
                ('track', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('_date', models.DateField(null=True)),
            ],
        ),
    ]
