# Generated by Django 3.2.6 on 2021-08-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_companypost'),
    ]

    operations = [
        migrations.AddField(
            model_name='companypost',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]