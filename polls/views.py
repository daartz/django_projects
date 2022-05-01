from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from .forms import ClientForm,SocieteForm, RefClientForm,StatutForm, MissionForm,FactureForm

from .models import Choice, Question, Client, Mission, Facture, Statut, RefClient,Societe

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# CLIENT
class ClientView(generic.ListView):
    template_name = 'polls/clients.html'
    context_object_name = 'client_list'
    def get_queryset(self):
        return Client.objects.values()

class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('polls:client')

class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('polls:client')

class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('polls:client')


# MISSION
class MissionView(generic.ListView):
    template_name = 'polls/missions.html'
    context_object_name = 'mission_list'
    def get_queryset(self):
        return Mission.objects.values()

class MissionCreate(LoginRequiredMixin, CreateView):
    model = Mission
    fields = '__all__'
    success_url = reverse_lazy('polls:mission')

class MissionUpdate(LoginRequiredMixin, UpdateView):
    model = Mission
    fields = '__all__'
    success_url = reverse_lazy('polls:mission')

class MissionDelete(LoginRequiredMixin, DeleteView):
    model = Mission
    fields = '__all__'
    success_url = reverse_lazy('polls:mission')


# STATUT
class StatutView(generic.ListView):
    template_name = 'polls/statuts.html'
    context_object_name = 'statut_list'
    def get_queryset(self):
        return Statut.objects.values()

class StatutCreate(LoginRequiredMixin, CreateView):
    model = Statut
    fields = '__all__'
    success_url = reverse_lazy('polls:statut')

class StatutUpdate(LoginRequiredMixin, UpdateView):
    model = Statut
    fields = '__all__'
    success_url = reverse_lazy('polls:statut')

class StatutDelete(LoginRequiredMixin, DeleteView):
    model = Statut
    fields = '__all__'
    success_url = reverse_lazy('polls:statut')


# FACTURE
class FactureView(generic.ListView):
    template_name = 'polls/factures.html'
    context_object_name = 'facture_list'
    def get_queryset(self):
        return Facture.objects.values()

class FactureCreate(LoginRequiredMixin, CreateView):
    model = Facture
    fields = '__all__'
    success_url = reverse_lazy('polls:facture')

class FactureUpdate(LoginRequiredMixin, UpdateView):
    model = Facture
    fields = '__all__'
    success_url = reverse_lazy('polls:facture')

class FactureDelete(LoginRequiredMixin, DeleteView):
    model = Facture
    fields = '__all__'
    success_url = reverse_lazy('polls:facture')


# REFCLIENT
class RefClientView(generic.ListView):
    template_name = 'polls/refclients.html'
    context_object_name = 'statut_list'
    def get_queryset(self):
        return RefClient.objects.values()

class RefClientCreate(LoginRequiredMixin, CreateView):
    model = RefClient
    fields = '__all__'
    success_url = reverse_lazy('polls:refclient')

class RefClientUpdate(LoginRequiredMixin, UpdateView):
    model = RefClient
    fields = '__all__'
    success_url = reverse_lazy('polls:refclient')

class RefClientDelete(LoginRequiredMixin, DeleteView):
    model = RefClient
    fields = '__all__'
    success_url = reverse_lazy('polls:refclient')


# SOCIETE
class SocieteView(generic.ListView):
    template_name = 'polls/societes.html'
    context_object_name = 'societe_list'
    def get_queryset(self):
        return Societe.objects.values()

class SocieteCreate(LoginRequiredMixin, CreateView):
    model = Societe
    fields = '__all__'
    success_url = reverse_lazy('polls:societe')

class SocieteUpdate(LoginRequiredMixin, UpdateView):
    model = Societe
    fields = '__all__'
    success_url = reverse_lazy('polls:societe')

class SocieteDelete(LoginRequiredMixin, DeleteView):
    model = Societe
    fields = '__all__'
    success_url = reverse_lazy('polls:societe')


def owner(request):
    return HttpResponse("Hello, world. 2bd19fb4 is the polls index.")

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))