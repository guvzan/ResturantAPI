from django.db import models


class Resturant(models.Model):
    name = models.CharField()
    password = models.CharField()
    active_menu = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Menu(models.Model):
    main = models.CharField()
    salad = models.CharField()
    dessert = models.CharField()
    drink = models.CharField()
    for_day = models.IntegerField(default=0)
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE)
