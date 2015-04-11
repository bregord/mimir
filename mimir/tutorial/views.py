from django.shortcuts import render, render_to_response
from django.conf.urls import url, patterns
import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def editorPage(request):
	#title = request.POST['title']

	if request.method == "POST":
        data = UserForm(request.POST)
		context_dict = {'form': data }# 'preservedText': data}

        return render_to_response('tutorial.html',context_dict, context_instance=RequestContext(request))

	form = forms.editorPageForm()
	content = ''
	context_dict = {'form': form, 'content': content}
	return render_to_response('tutorial.html',context_dict, context_instance=RequestContext(request))
   

