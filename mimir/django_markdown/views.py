""" Supports preview. """
from django.core.files.storage import default_storage
from django.shortcuts import render, render_to_response
from django.template import RequestContext


from . import settings


def preview(request):
    """ Render preview page.

    :returns: A rendered preview

    """
    if settings.MARKDOWN_PROTECT_PREVIEW:
        user = getattr(request, 'user', None)
        if not user or not user.is_staff:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())

    content=request.REQUEST.get('data', 'No content posted')
    inputText=request.POST.get('data')
    titleText=request.POST.get('Title')
    #descText=request.POST.get('description')
    context_dict = {'content': content, "inputText":inputText, "titleText":titleText}#, "descText":descText}

    return render_to_response(settings.MARKDOWN_PREVIEW_TEMPLATE,context_dict, context_instance=RequestContext(request))
    #return render(request, settings.MARKDOWN_PREVIEW_TEMPLATE, context_dict)