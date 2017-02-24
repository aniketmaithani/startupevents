# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from versatileimagefield.fields import VersatileImageField
from uuid_upload_path import upload_to
from ..customuser.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    mobile = models.CharField(max_length=10, blank=False, null=True)
    work_location = models.TextField(
        null=True, blank=True, verbose_name=u"Present Company")
    work_experience = models.FloatField(
        null=True, blank=True, verbose_name=u"Work Experience")
    github = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    googleplus = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    personal_blog = models.URLField(null=True, blank=True)
    organization_website = models.URLField(null=True, blank=True)
    profile_pic = VersatileImageField(
        blank=True, null=True, upload_to=upload_to)

    def __str__(self):
        return '{}'.format(self.user)
