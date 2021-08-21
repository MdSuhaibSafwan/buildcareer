# Generated by Django 3.2.6 on 2021-08-21 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lib.base_model


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_companypost_open'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0003_auto_20210821_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobInvites',
            fields=[
                ('id', models.UUIDField(default=lib.base_model.uuid_without_dash, editable=False, primary_key=True, serialize=False, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('slug', models.SlugField(default=lib.base_model.random_number_gen, editable=False)),
                ('description', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('company_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_invites', to='company.companypost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_invited', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'company_post')},
            },
        ),
    ]
