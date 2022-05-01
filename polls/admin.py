from django.contrib import admin

from .models import Question,  Choice, Client, Mission, Facture, RefClient, Statut, Societe

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Client)
admin.site.register(Mission)
admin.site.register(Facture)
admin.site.register(RefClient)
admin.site.register(Statut)
admin.site.register(Societe)