from django.shortcuts import render, render_to_response
from django.conf.urls import url, patterns
import forms
<<<<<<< HEAD
from datetime import datetime
=======
import datetime
>>>>>>> efeb02e0215f27fdb50f834c234c7823ad9119dc
from forum.models import Seminar
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
#import django.contrib.auth.models.User
# Create your views here.
from django.contrib.auth.decorators import login_required


#@login_required
def editorPage(request):
	#title = request.POST['title']

	form = forms.editorPageForm()

	if request.method == "POST":
		data = request.POST.get("input")
		title = request.POST.get("title")
		#description = request.POST.get("description")
		context_dict = {'form': form,'content': data, 'title':title}#, "description":description}
		return render_to_response('tutorial.html',context_dict, context_instance=RequestContext(request))

	context_dict = {'form': form}
	return render_to_response('composition.html',context_dict, context_instance=RequestContext(request))

def savePage(request):
	if request.method == "POST":
		if request.user.is_authenticated():
			username = request.user
			title = request.POST.get('title')
			seminar = Seminar(author = request.user, 
				title = title,
				contents = request.POST.get('input'), 
				date = datetime.datetime.now(),
				description= "test"  )
			seminar.save()
			print "Title"
			print title
			return HttpResponseRedirect("/user/{0}/{1}/".format(username,title))

		else:
			return HttpResponseRedirect("/")

		