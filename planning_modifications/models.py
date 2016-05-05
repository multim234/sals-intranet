from django.db import models


class Modification(models.Model):
    related_classe = models.CharField(max_length=256)
    related_staff = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)
    info = models.TextField()

    def __str__(self):
        return "-" + self.related_staff
