from django.shortcuts import render
from django.conf.urls import url, patterns
import forms
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

'''def editorPage(request):
   # context = RequestContext(request)
    form = editorPageForm()
    context_dict = {'form': form}
    #return render_to_response('tutorial.html', context_dict, context)

    return render_to_response('tutorial.html',context_dict, context_instance=RequestContext(request))
   '''
def editorPage(request, error=""):
	if request.method == "POST":
		return HttpResponseRedirect("/index/")
	else:
		return render_to_response('registration.html',{'error':''}, context_instance=RequestContext(request))