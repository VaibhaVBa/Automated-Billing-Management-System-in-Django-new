# Generated by Django 4.0.3 on 2022-04-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmain',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]