from django.db import models
# Create your models here.

class Person(models.Model):
    MEMORY = (
        ('Sim', 'Sim'),
        ('Phone', 'Phone'),
    )
    name = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=20, null=True, choices=MEMORY)
    
    def __str__(self):
        return self.name

class Sim(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.person.name
    
class Phone(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.person.name