from django.db import models
from projects.models import Project

class ProjectView(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.ip_address}"