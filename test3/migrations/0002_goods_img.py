# Generated by Django 2.1.3 on 2018-11-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='img',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
