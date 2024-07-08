from django.db import models


class Details(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.first_name
