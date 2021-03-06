# Generated by Django 2.1.3 on 2018-11-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goodid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=11)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField()),
            ],
        ),
    ]
