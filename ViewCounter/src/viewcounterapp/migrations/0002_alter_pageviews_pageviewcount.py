# Generated by Django 4.1 on 2022-09-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("viewcounterapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pageviews",
            name="pageViewCount",
            field=models.IntegerField(default=0),
        ),
    ]
