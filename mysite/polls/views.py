# For stub methods for detail, result and vote
from django.http import HttpResponse, Http404
# This is a convenient method render()
from django.shortcuts import render
from polls.models import Poll

def index(req):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(req, 'polls/index.html', context)

def detail(req, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(req, 'polls/detail.html', {'poll':poll})

def results(req, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(req, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
