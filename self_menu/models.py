from django.db import models
from datetime import datetime


class Lunch_menu(models.Model):
    lunch_date = models.DateField(unique_for_date="lunch_date")

    midday_entrance = models.CharField(max_length=256)
    midday_dish = models.CharField(max_length=256)
    midday_dessert = models.CharField(max_length=256)

    dinner_entrance = models.CharField(max_length=256, blank=True, null=True)
    dinner_dish = models.CharField(max_length=256, blank=True, null=True)
    dinner_dessert = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return "lunch for : " + "{0}".format(self.lunch_date)

    def get_next_dinner(self):
        if(datetime.now().hour < 12):
            if self.midday_entrance and self.midday_dish and self.midday_dessert:
                return (self.midday_entrance, self.midday_dish, self.midday_dessert)
            else:
                return ("Not defined", "not defined", "not defined")
        else:
            if self.dinner_entrance and self.dinner_dish and self.dinner_dessert:
                return (self.dinner_entrance, self.dinner_dish, self.dinner_dessert)
            else:
                return ("Not defined", "not defined", "not defined")
