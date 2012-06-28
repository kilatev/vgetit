from django.db import models

class Podcasts(models.Model):
    rss = models.TextField()