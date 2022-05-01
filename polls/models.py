import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Societe(models.Model):
    raison_sociale = models.CharField(max_length = 200)
    date_creation =models.DateTimeField('date creation')
    adresse1 = models.CharField(max_length = 200)
    adresse2 = models.CharField(max_length = 200, blank=True, null=True)
    cp_ville = models.CharField(max_length = 200, blank=True, null=True, default="_")
    siren =models.CharField(max_length = 9,default=0, blank=True, null=True)
    siret =models.CharField(max_length = 14,default=0, blank=True, null=True)
    num_tva_intra =models.CharField(max_length = 13,default=0, blank=True, null=True)
    code_naf=models.CharField(max_length = 5,default=0, blank=True, null=True)
    capital_social=models.IntegerField(default=0, blank=True, null=True)
    representant =models.CharField(max_length = 200, blank=True, null=True, default="_")
    telephone =models.CharField(max_length = 15,default=0, blank=True, null=True)
    mail=models.CharField(max_length = 50, blank=True, null=True, default="_")
    def __str__(self):
        return self.raison_sociale

class Client(models.Model):
    raison_sociale = models.CharField(max_length = 200)
    adresse1 = models.CharField(max_length = 200)
    adresse2 = models.CharField(max_length = 200)
    cp_ville = models.CharField(max_length = 200, blank=True, null=True, default="_")
    interlocuteur =models.CharField(max_length = 200, blank=True, null=True, default="_")
    telephone =models.CharField(max_length = 15,default=0, blank=True, null=True)
    mail=models.CharField(max_length = 200, blank=True, null=True, default="_")
    def __str__(self):
        return self.raison_sociale

class Mission(models.Model):
    type_mission=models.CharField(max_length=200)
    def __str__(self):
        return self.type_mission

class RefClient(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ref_client = models.CharField(max_length=200)
    def __str__(self):
        return self.ref_client

class Statut(models.Model):
    statut=models.CharField(max_length=200)
    def __str__(self):
        return self.statut

class Facture(models.Model):
     num_facture=models.IntegerField()
     date_edit=models.DateTimeField('date edition')
     id_societe = models.ForeignKey(Societe, on_delete=models.CASCADE,default=0)
     id_refclient = models.ForeignKey(RefClient, on_delete=models.CASCADE)
     id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
     id_mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
     activite = models.CharField(max_length = 200)
     montant_HT =models.IntegerField(default=0)
     remb_frais =models.IntegerField(default=0, blank=True, null=True)
     taux_TVA =models.IntegerField(default=0, blank=True, null=True)
     montant_TVA =models.IntegerField(default=0, blank=True, null=True)
     montant_TTC =models.IntegerField(default=0)
     id_statut = models.ForeignKey(Statut, on_delete=models.CASCADE, default=0)



