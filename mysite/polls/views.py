# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll

def index(req):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(req, {
            'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def detail(req, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(req, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(req, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
