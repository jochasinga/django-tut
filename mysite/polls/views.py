# Create your views here.
from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render
from polls.models import Poll

def index(req):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(req, 'polls/index.html', context)

def detail(req, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(req, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(req, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
