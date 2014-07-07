from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from dblog.dblog_obj import DBlog
dblog = DBlog()

def basic(request):


    t = loader.get_template('htdocs/basic.html')
    c = RequestContext( request,{})
    return HttpResponse(t.render(c))