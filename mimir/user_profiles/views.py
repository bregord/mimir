from django.shortcuts import render, render_to_response
from registration.models import UserProfile
from forum.models import Seminar
from django.contrib.auth.models import User
from django.template import RequestContext


import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class MyRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code.strip())
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)



# Create your views here.

def profile(request, username):
        if 's' in request.GET:
                return show(request, username, request.GET['s'])
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

def show(request, username, seminar_title):
        print "username"
	user = User.objects.get(username=username)
	seminars = Seminar.objects.filter(author=user)
	seminar = [ seminar for seminar in seminars if seminar.title == seminar_title ][0]
        renderer = MyRenderer()
        md = mistune.Markdown(renderer=renderer)
	context = { 'seminar' : seminar , 'contents' : md.render(seminar.contents) }
        return render_to_response('show.html', context, context_instance=RequestContext(request))
	
