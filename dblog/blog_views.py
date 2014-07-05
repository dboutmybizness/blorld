from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404


def single_post(request, post_id):

    t = loader.get_template('dblog/base/single_post.html')
    c = RequestContext( request,{})
    return HttpResponse(t.render(c))

def main(request):

    t = loader.get_template('dblog/base/main.html')
    c = RequestContext( request,{})
    return HttpResponse(t.render(c))