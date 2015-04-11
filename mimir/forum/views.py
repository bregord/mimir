from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
        # nothing to do here for now
        return render_to_response('forum.html')
