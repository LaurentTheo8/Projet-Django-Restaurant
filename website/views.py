from django.shortcuts import render
from .forms import MessageForm, ReservationForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', {})

def contact(request):

    form = MessageForm(request.POST or None)
    envoi = False

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        envoi = True
        form.save()
        return HttpResponseRedirect("contact.html")

    return render(request, 'contact.html', locals())

def reservation(request):
    form = ReservationForm(request.POST or None)

    if form.is_valid():
        customer = form.cleaned_data['customer']
        nbPerson = form.cleaned_data['nbPerson']
        email = form.cleaned_data['email']
        date = form.cleaned_data['date']
        message = form.cleaned_data['message']

        envoi = True
        form.save()

        return HttpResponseRedirect("reservation.html")

    return render(request, 'reservation.html', locals())
