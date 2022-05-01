from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'hello'
urlpatterns = [
    # dj4e
    path('', views.hello, name='hello'),
    path('authz/', TemplateView.as_view(template_name='hello/main.html')),
    path('open', views.OpenView.as_view(), name='open'),
    path('apereo', views.ApereoView.as_view(), name='apereo'),
    path('protect', views.ProtectView.as_view(), name='protect'),
    path('python', views.DumpPython.as_view(), name='python'),

]