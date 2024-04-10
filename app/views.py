from django.shortcuts import render
from django import template
from django.template import loader
from django.http import JsonResponse,HttpResponse
# Create your views here.

def home(request):
    context ={}
    try:
        return render(request, 'home.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
    


def login(request):
    context ={}
    try:
        return render(request, 'user/login.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
    

def register(request):
    context ={}
    try:
        return render(request, 'user/register.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
    
def Userdashboard(request):
    context ={}
    try:
        return render(request, 'userdashboard.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
    

def Clusterdashboard(request):
    context ={}
    try:
        return render(request, 'userdashboard.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))