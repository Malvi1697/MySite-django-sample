from django.db import models

# Create your models here.


class PageVisit(models.Model):
    # id = hidden iteration
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.path}"
