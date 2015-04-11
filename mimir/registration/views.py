from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from registration.models import UserProfile

from .forms import *

# Create your views here.
def index(request):
        return render_to_response('index.html')

def register(request, error=""):
        if request.method == "POST":
                form = UserForm(request.POST) 
                if form.is_valid():
                        username    = form.cleaned_data['username']
                        password    = form.cleaned_data['password']
                        email       = form.cleaned_data['email']
                        description = form.cleaned_data['description']
                        website     = form.cleaned_data['website']
                        interests   = form.cleaned_data['interests']
                        # validate user
	                user = User.objects.filter(username = username)
	                if user.exists():
                                return render_to_response('registration.html',{ 'error' : 'UserProfilename taken!', 'form' : form}, context_instance=RequestContext(request))
	
	                user = User.objects.filter(email = email)
	                if user.exists():
                                return render_to_response('registration.html',{ 'error' : 'Email taken!', 'form' : form }, context_instance=RequestContext(request))
	                user = User.objects.create_user(username,email,password,)
	                user.save()
	                userProfile = UserProfile(user=user,description=description,website=website,interests=interests)
	                userProfile.save()
	                user = authenticate(username=username,password=password)
	                login(request,user)
	                return HttpResponseRedirect("/forum/")
        else:   
                form = UserForm()
                return render_to_response('registration.html',{'error':'', 'form': form}, context_instance=RequestContext(request))
                
