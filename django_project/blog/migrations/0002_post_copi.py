# Generated by Django 3.1.3 on 2020-11-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='coPI',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
