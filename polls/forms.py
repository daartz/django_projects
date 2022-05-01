from django import forms

from .models import Client, Societe, Facture, RefClient,Mission,Statut

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class SocieteForm(forms.ModelForm):
    class Meta:
        model = Societe
        fields = '__all__'

class RefClientForm(forms.ModelForm):
    class Meta:
        model = RefClient
        fields = ('id_client', 'ref_client')

class StatutForm(forms.ModelForm):
    class Meta:
        model = Statut
        fields = ('statut',)

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ('type_mission',)

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = '__all__'
