# Generated by Django 4.0.4 on 2022-04-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='depth',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='path',
            field=models.TextField(),
            preserve_default=False,
        ),
    ]
