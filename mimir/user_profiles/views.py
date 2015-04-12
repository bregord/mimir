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
        # Some realy dumb shit to make the templating work
        # Since muse made the HTML such that the first two seminars need to be treated differently than the rest, we have to deal with these cases
        semN = len(seminars)
       
        if semN == 0:
                sem_1 = False
                sem_2 = False
                sems = []
        elif semN == 1:
                sem_1 = seminars[0]
                sem_2 = False
                sems = []
        elif semN >= 2:
                sem_1 = seminars[0]
                sem_2 = seminars[1]
                sems = seminars[2:]

        interests = userProfile.interests.split(";")
        context = { 'sem_1' : sem_1, 'sem_2' : sem_2, 'sems' : sems, 'user' : user, 'interests' : interests, 'userProfile' : userProfile}
        return render_to_response('user.html', context, context_instance=RequestContext(request))
