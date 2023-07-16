from requests import Request, request
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect


def index(request):

    hostTenant = request.headers['Host']
    front = "http://www.localhost:3000"
    more = "/"
    return HttpResponseRedirect(front + more + hostTenant)


# Create your views here.
