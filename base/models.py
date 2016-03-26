from django.db import models


class Message(models.Model):
    texte = models.CharField(max_length=256)
    time_to_show = models.IntegerField(default=10)

    def __str__(self):
        return self.texte
