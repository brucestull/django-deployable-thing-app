# things/models.py

from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Thing"
        verbose_name_plural = "Things"
        ordering = ["-created_at"]
