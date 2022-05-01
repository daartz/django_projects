from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),

    # CLIENT
    # ex: /polls/clients/
    path('clients/', views.ClientView.as_view(), name='client'),
    path('clients/create/', views.ClientCreate.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', views.ClientUpdate.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', views.ClientDelete.as_view(), name='client_delete'),

    # MISSION
    # ex: /polls/missions/
    path('missions/', views.MissionView.as_view(), name='mission'),
    path('missions/create/', views.MissionCreate.as_view(), name='mission_create'),
    path('missions/<int:pk>/update/', views.MissionUpdate.as_view(), name='mission_update'),
    path('missions/<int:pk>/delete/', views.MissionDelete.as_view(), name='mission_delete'),

    # SOCIETE
    # ex: /polls/societes/
    path('societes/', views.SocieteView.as_view(), name='societe'),
    path('societes/create/', views.SocieteCreate.as_view(), name='societe_create'),
    path('societes/<int:pk>/update/', views.SocieteUpdate.as_view(), name='societe_update'),
    path('societes/<int:pk>/delete/', views.SocieteDelete.as_view(), name='societe_delete'),

    # STATUT
    # ex: /polls/statuts/
    path('statuts/', views.StatutView.as_view(), name='statut'),
    path('statuts/create/', views.StatutCreate.as_view(), name='statut_create'),
    path('statuts/<int:pk>/update/', views.StatutUpdate.as_view(), name='statut_update'),
    path('statuts/<int:pk>/delete/', views.StatutDelete.as_view(), name='statut_delete'),


    # FACTURE
    # ex: /polls/factures/
    path('factures/', views.FactureView.as_view(), name='facture'),
    path('factures/create/', views.FactureCreate.as_view(), name='facture_create'),
    path('factures/<int:pk>/update/', views.FactureUpdate.as_view(), name='facture_update'),
    path('factures/<int:pk>/delete/', views.FactureDelete.as_view(), name='facture_delete'),


    # REFCLIENT
    # ex: /polls/refclients/
    path('refclients/', views.RefClientView.as_view(), name='refclient'),
    path('refclients/create/', views.RefClientCreate.as_view(), name='refclient_create'),
    path('refclients/<int:pk>/update/', views.RefClientUpdate.as_view(), name='refclient_update'),
    path('refclients/<int:pk>/delete/', views.RefClientDelete.as_view(), name='refclient_delete'),


    # dj4e
    path('owner', views.owner, name='owner'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]