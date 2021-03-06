# Generated by Django 3.0.5 on 2020-12-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieCd', models.IntegerField(primary_key=True, serialize=False)),
                ('movieNm', models.CharField(max_length=20)),
                ('openDt', models.CharField(max_length=10)),
                ('typeNm', models.CharField(max_length=3)),
                ('nationAlt', models.CharField(max_length=5)),
                ('genreAlt', models.CharField(max_length=40)),
                ('directors', models.CharField(max_length=20)),
                ('showTm', models.CharField(max_length=5)),
                ('userRating', models.CharField(max_length=8)),
            ],
        ),
    ]
