from django.shortcuts import render, render_to_response
from django.conf.urls import url, patterns
import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def editorPage(request):
	#title = request.POST['title']

	form = forms.editorPageForm()

	if request.method == "POST":
		data = request.POST.get("input")
		title = request.POST.get("Title")
		#description = request.POST.get("description")
		context_dict = {'form': form,'content': data, 'title':title}#, "description":description}
		return render_to_response('tutorial.html',context_dict, context_instance=RequestContext(request))

	context_dict = {'form': form}
	return render_to_response('tutorial.html',context_dict, context_instance=RequestContext(request))
   

