from django.contrib import admin

# Register your models here.
from . models import Person
from .models import Sim 
from .models import Phone

admin.site.register(Person)
admin.site.register(Sim)
admin.site.register(Phone)