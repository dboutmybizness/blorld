from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404


def home(request):

    t = loader.get_template('dblog/base/home.html')
    c = RequestContext( request,{})
    return HttpResponse(t.render(c))