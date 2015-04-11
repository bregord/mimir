from django.shortcuts import render, render_to_response
from registration.models import UserProfile
from forum.models import Seminar
from django.contrib.auth.models import User
from django.template import RequestContext


# Create your views here.

def profile(request, username):
        user = User.objects.get(username=username)

        seminars = Seminar.objects.all().filter(author=user)

        context = { 'seminars' : seminars, 'user' : user.username}
        print username
        return render_to_response('user.html', context, context_instance=RequestContext(request))

def showSeminar(request, username, seminar_title):
	user = User.objects.get(username=username)

	seminar = Seminar.objects.filter(author=user).filter(for seminar in Seminar if seminar.title==seminar_title)[0]
	context = { 'seminars' : seminars, 'user' : user.username, 'title' : seminar.title}
	