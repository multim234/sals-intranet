from django.db import models


class Missing(models.Model):
    staff_name = models.CharField(max_length=256)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.staff_name
