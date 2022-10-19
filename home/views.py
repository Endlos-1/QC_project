from re import template
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def agent_Faq(request):
    return render(request, 'home/agentFaq.html')


def broker_Faq(request):
    return render(request, 'home/brokerFaq.html')


def applynow(request):
    return render(request, 'home/applynow.html')

def contactUs(request):
    return render(request, 'home/contactUs.html')

def aboutUs(request):
    return render(request, 'home/aboutUs.html')