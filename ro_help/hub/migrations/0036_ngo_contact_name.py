# Generated by Django 3.0.4 on 2020-03-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0035_auto_20200328_1651"),
    ]

    operations = [
        migrations.AddField(
            model_name="ngo",
            name="contact_name",
            field=models.CharField(default="", max_length=254, verbose_name="Contact person's name"),
            preserve_default=False,
        ),
    ]
