from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    id_no = models.CharField(max_length=255)
    location_id = models.BigIntegerField()
    campaign_id = models.PositiveIntegerField(blank=True, null=True)
    level_id = models.BigIntegerField(blank=True, null=True)
    role_id = models.IntegerField()
    org_types_id = models.BigIntegerField()
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    has_smartphone = models.BooleanField(default=False)
    job_group = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=True)
    sync_status = models.BooleanField(default=False)
    deactivated_by = models.BigIntegerField(blank=True, null=True)
