from django.http import Http404
from django.http import HttpResponseForbidden


def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404

def check_topic_public(topic, request):
    if topic.public != True:
        raise HttpResponseForbidden