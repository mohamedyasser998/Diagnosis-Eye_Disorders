# Generated by Django 3.0.3 on 2021-07-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20210707_1035"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="illness",
            field=models.ManyToManyField(blank=True, to="diagnose.Illness"),
        ),
    ]