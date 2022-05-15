from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title, self.url

class URLWarning(models.Model):
    warningsmessage = "This URL is unsafe"
    def __str__(self):
        return f"{self.warningmessage}"

class URLSafe(models.Model):
    warningsmessage = "This URL is Safe"
    def __str__(self):
        return f"{self.safemessage}"
