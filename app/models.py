from django.db import models

class Snippet(models.Model):
    code = models.TextField()
    created = models.DateTimeField(auto_now=True)
    score = models.FloatField(default=1600.0)
    image_url = models.URLField(null=True)
    author = models.CharField(max_length=32, null=False)
    #  status = models.
