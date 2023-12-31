from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField()
    booking_date = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title
    
    def save_menu(self):
        self.save()

    def delete_menu(self):
        self.delete()
