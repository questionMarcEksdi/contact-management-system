from django import http
from django.db.models.query import QuerySet
from django.forms.models import modelformset_factory
# from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .form import personForm
from .models import (Person, Phone, Sim)

# from django.http import  HttpResponse




# Create your views here.

def home(request):
    contact = Person.objects.all()
    context = {
        'contacts': contact
    }
    return render(request, 'contacts/display_contact.html', context)

def details(request, pk):
    person = Person.objects.get(id=pk)
    context = {
        'person': person
        
    }
    return render(request, 'contacts/display_contact_info.html', context)

def addContact(request):
    if request.method == 'POST':
        formset = personForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    else:
        formset = personForm()
    
    return render(request, 'contacts/add_contact.html', {'formset': formset})
    
def updateContact(request, pk):
    person = Person.objects.get(id=pk)
    formset = personForm(instance=person)
    if request.method == 'POST':
        formset = personForm(request.POST, instance=person)
        
        if formset.is_valid():
            formset.save()
            return redirect("/")
    
    return render(request, 'contacts/update_contact.html', {'formset': formset})
        
def deleteContact(request, pk):
    person = Person.objects.get(id=pk)
    if request.method == 'POST':
        person.delete()
        return redirect("/")
        
    context = {
         'person': person,
    }
    return render(request, 'contacts/delete_contact.html',context)