# Generated by Django 2.2.2 on 2019-06-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libsys', '0006_auto_20190525_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
