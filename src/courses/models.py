from django.db import models

"""
- Courses:
    - Title
    - Description
    - Thumnail/Image
    - Access:
        - Anyone
        - Email required
        - Purchase required
        - User required (n/a)
    - Status:
        - Published
        - Coming Soon
        - Draft
"""

class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image
    access = models.CharField(
        max_length=5,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
        )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    
    @property
    def is_published(self):
        return self.s
        COMtatus == PublishStatus.PUBLISHED


"""
- Lessons:
    - Title
    - Description
    - Video
    - Status: Published, Coming Soon, Draft
"""