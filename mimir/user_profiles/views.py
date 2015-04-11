from django.shortcuts import render, render_to_response
from registration.models import UserProfile
from forum.models import Seminar
from django.contrib.auth.models import User
from django.template import RequestContext


# Create your views here.

def profile(request, username):
        user = User.objects.get(username=username)
        userProfile = UserProfile.objects.get(user=user)
        seminars = Seminar.objects.all().filter(author=user)
        interests = userProfile.interests.split(";")
        context = { 'seminars' : seminars, 'user' : user, 'interests' : interests, 'userProfile' : userProfile}
        print username
        return render_to_response('user.html', context, context_instance=RequestContext(request))
