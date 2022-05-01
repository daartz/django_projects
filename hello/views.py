
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

def hello(request):
    num=request.session.get('num_visits',0)+1
    request.session["num_visits"]=num
    res = HttpResponse("view count="+str(num))
    res.set_cookie('dj4e_cookie', '2bd19fb4', max_age=1000)
    return res

class OpenView(View) :
    def get(self, request):
        return render(request, 'hello/main.html')

class ApereoView(View) :
    def get(self, request):
        return render(request, 'hello/main.html')

class ProtectView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'hello/main.html')

class DumpPython(View) :
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/authz">Go back</a>"""
        return HttpResponse(resp)
