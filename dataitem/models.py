from django.db import models
from django.contrib.auth.models import User

class Dataitem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    uploaded_file = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
