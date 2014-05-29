from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse
from polls.models import Poll
from django.template import RequestContext, loader

def index(request):
    latest=Poll.objects.order_by('pub_date')
    template= loader.get_template('latest.html')
    context = RequestContext(request,{
        'latest': latest,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    return render(request,'detail.html',{'poll':poll})

def result(request,poll_id):
    return HttpResponse("result is:" % poll_id)

def vote(request, poll_id):
    return HttpResponse("you are voting" % poll_id)
# Create your views here.

