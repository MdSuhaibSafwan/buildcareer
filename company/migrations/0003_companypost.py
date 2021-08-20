# Generated by Django 3.2.6 on 2021-08-20 09:01

from django.db import migrations, models
import django.db.models.deletion
import lib.base_model


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPost',
            fields=[
                ('id', models.UUIDField(default=lib.base_model.uuid_without_dash, editable=False, primary_key=True, serialize=False, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('post', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=350)),
                ('slug', models.SlugField(default=lib.base_model.random_number_gen)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'ordering': ['-timestamp'],
                'abstract': False,
            },
        ),
    ]
