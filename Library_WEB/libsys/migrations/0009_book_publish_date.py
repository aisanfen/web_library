# Generated by Django 2.2.2 on 2019-06-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libsys', '0008_book_publish_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(null=True),
        ),
    ]
