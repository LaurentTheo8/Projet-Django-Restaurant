from django import forms
from .models import Message, Reservation

class MessageForm(forms.ModelForm):
    class Meta :
        model = Message
        fields = ['name', 'subject', 'email', 'message']


        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Full Name','name':'Name','id':'cf-name','class':'form-control'}),
                   "subject":forms.TextInput(attrs={'placeholder':'subject','name':'subject','id':'cf-subject','class':'form-control'}),
                   "email":forms.TextInput(attrs={'placeholder':'email','name':'email','id':'cf-email','class':'form-control'}),
                   "message":forms.Textarea(attrs={'placeholder':'Your message','name':'message','id':'cf-message','class':'form-control', 'rows':'4'}),
                }

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):

    class Meta :
        model = Reservation
        fields = ['customer', 'nbPerson', 'email', 'message','date']

        widgets={
                   "customer":forms.TextInput(attrs={'placeholder':'Full Name','name':'customer','id':'cf-customer','class':'form-control'}),
                   "nbPerson":forms.TextInput(attrs={'placeholder':'Number of persons ?','name':'nbPerson','id':'cf-nbPerson','class':'form-control'}),
                   "email":forms.TextInput(attrs={'placeholder':'email','name':'email','id':'cf-email','class':'form-control'}),
                   "message":forms.Textarea(attrs={'placeholder':'A message ?','name':'message','id':'cf-message','class':'form-control', 'rows':'4'}),
                   "date": DateInput(attrs={'id':'cf-date'})
                }


