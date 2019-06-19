from django.db import models

class Customer(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Application(models.Model):
  name = models.CharField(max_length=200)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

  def __str__(self):
    return self.name