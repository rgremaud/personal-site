from django.conf import settings
from django.db import models
from django.urls import reverse

class Project(models.Model):
    """Project model for overall blog."""
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    """Comments to link with each project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("project_list")