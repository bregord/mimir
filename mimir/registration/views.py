from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from registration.models import UserProfile

# Create your views here.
def index(request):
        return render_to_response('landing/index.html',{})

def register(request, error=""):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                email    = request.POST['email']
                # validate user
                user = User.objects.filter(username = username)
                if user.exists():
                        return render_to_response('registration.html',{ 'error' : 'UserProfilename taken!'}, context_instance=RequestContext(request))

                user = User.objects.filter(email = email)
                if user.exists():
                        return render_to_response('registration.html',{ 'error' : 'Email taken!' }, context_instance=RequestContext(request))
                user = User.objects.create_user(username,email,password)
                user.save()
                userProfile = UserProfile(user=user)
                userProfile.save()
                user = authenticate(username=username,password=password)
                login(request,user)
                return HttpResponseRedirect("/forum/")
        else:   
                return render_to_response('registration.html',{'error':''}, context_instance=RequestContext(request))
                
