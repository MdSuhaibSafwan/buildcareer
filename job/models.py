from django.db import models, IntegrityError
from lib.base_model import BaseModel, random_number_gen
from django.utils import timezone
from company.models import CompanyPost
from django.contrib.auth import get_user_model

User = get_user_model()


class JobRequest(BaseModel):
    """
    THIS MODEL IS FOR JOB REQUEST BY A USER...
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_requests")
    company_post = models.ForeignKey(CompanyPost, on_delete=models.CASCADE, related_name="jobs")
    slug = models.SlugField(default=random_number_gen, editable=False)
    description = models.TextField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} request --> {self.company_post}"

    class Meta:
        unique_together = ["user", "company_post"]


class JobRequestAttachment(BaseModel):
    """
    THIS MODEL IS TO ATTACH FILES WITH JOB REQUEST POSTS
    """
    job_request = models.ForeignKey(JobRequest, on_delete=models.SET_NULL, 
                                    null=True, related_name="attachments")
    attachment = models.FileField()

    def __str__(self):
        return self.job_request.user.username + " Job Attachment"

    def save(self, *args, **kwargs):
        att = self.job_request.attachments.count()
        if att >= 10:
            raise IntegrityError("Not more than 10 files are allowed")
        return super().save(*args, **kwargs)


class JobInvites(BaseModel):
    """
    THIS MODEL IS FOR JOB INVITE BY A COMPANY...
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_invited")
    company_post = models.ForeignKey(CompanyPost, on_delete=models.CASCADE, related_name="job_invites")
    slug = models.SlugField(default=random_number_gen, editable=False)
    description = models.TextField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} invite --> {self.company_post}"

    class Meta:
        unique_together = ["user", "company_post"]    

