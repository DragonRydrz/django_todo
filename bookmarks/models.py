from django.db import models

# Create your models here.


class Bookmark(models.Model):
    site = models.CharField(max_length=64)
    address = models.URLField()

    def __str__(self):
        return self.site


# class PrivateBookmark(Bookmark):
#     private = models.BooleanField(default=True)
