from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="contacts"), #this will call views.home(request)
    path('details/<int:pk>', views.details, name="details") # this would call the function views.view(request, pk=N) where N is the id number of an object in the database
    ,
    path('new', views.addContact, name="new"),
    path('update/<int:pk>', views.updateContact, name="update"),
    path('delete/<int:pk>', views.deleteContact, name="delete"),
]
