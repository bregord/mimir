from django.shortcuts import render, render_to_response
from .models import * 


class SemTem():
        def __init__(self, author,title,preview, date):
                self.author  = author
                self.title   = title
                self.preview = preview
                self.date = date

# Create your views here.
def index(request):
        # nothing to do here for now
        user = request.user
        seminars = [ SemTem(seminar.author,seminar.title,seminar.contents[:1233], seminar.date) for seminar in Seminar.objects.all() ]
        
        return render_to_response('forum.html', {'seminars' : seminars} )
