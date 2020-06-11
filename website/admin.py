from django.contrib import admin
from django.utils.text import Truncator

from .models import Message, Reservation

# Register your models here.

class MessageAdmin(admin.ModelAdmin):

    list_display = ('name','subject','email','date', 'apercu_contenu')
    list_filter = ('name','subject','email', 'date')
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('name','subject','email' )

    def apercu_contenu(self, message):
        return Truncator(message.message).chars(40, truncate='...')

    apercu_contenu.short_description = 'Aperçu du contenu'


def make_validate(self, request, queryset):
    queryset.update(validate='Y')
make_validate.short_description = "Validate a reservation"

class ReservationAdmin(admin.ModelAdmin):

    list_display = ('customer','nbPerson','email','date', 'apercu_contenu', 'validate')
    list_filter = ('customer','nbPerson','email', 'date')
    date_hierarchy = 'date'
    ordering = ('validate','date' )
    search_fields = ('validate','customer','date' )
    actions = [make_validate]

    def apercu_contenu(self, message):
        return Truncator(message.message).chars(40, truncate='...')

    apercu_contenu.short_description = 'Aperçu du contenu'





admin.site.register(Message, MessageAdmin)
admin.site.register(Reservation, ReservationAdmin)


