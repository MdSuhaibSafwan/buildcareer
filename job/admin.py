from django.contrib import admin
from .models import JobRequest, JobRequestAttachment, JobInvites

admin.site.register(JobRequest)
admin.site.register(JobRequestAttachment)
admin.site.register(JobInvites)
