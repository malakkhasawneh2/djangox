from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Snack(models.Model):
    title = models.CharField(max_length=255)
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.CharField(max_length=511)


    def get_absolute_url(self):

        return reverse('snack_detail', args=[self.id])

    def __str__(self):
        return self.title