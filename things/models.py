# things/models.py

from django.urls import reverse
from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse("things:thing_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Thing"
        verbose_name_plural = "Things"
        ordering = ["-created_at"]
