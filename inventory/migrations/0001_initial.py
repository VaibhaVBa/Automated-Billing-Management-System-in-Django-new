# Generated by Django 4.0.3 on 2022-04-18 09:20

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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('phone', models.IntegerField(default=0)),
                ('problem', models.CharField(max_length=1264)),
            ],
        ),
        migrations.CreateModel(
            name='ItemMain',
            fields=[
                ('itemid', models.AutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=50)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=25)),
                ('composition', models.TextField()),
                ('manufacturingdate', models.DateField()),
                ('expirydate', models.DateField()),
                ('quantity', models.IntegerField(default=0)),
                ('slug', models.SlugField(default='', editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('itemid', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='inventory.itemmain')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='itemmain',
            name='type',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='inventory.itemscat'),
        ),
    ]