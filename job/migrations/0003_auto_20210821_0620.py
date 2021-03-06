# Generated by Django 3.2.6 on 2021-08-21 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0004_companypost_open'),
        ('job', '0002_alter_jobrequestattachment_job_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='company_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='company.companypost'),
        ),
        migrations.AlterField(
            model_name='jobrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
