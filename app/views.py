from django.shortcuts import render
from django import template
from django.template import loader
from django.http import JsonResponse,HttpResponse
# Create your views here.

def Commingsoon(request):
    context ={}
    try:
        return render(request, 'comming_soon.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

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
    
def about(request):
    context ={}
    try:
        return render(request, 'about.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

def mixed_wast(request):
    context ={}
    try:
        return render(request, 'services/mixed_waste.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')

def metals(request):
    context ={}
    try:
        return render(request, 'services/matels.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')

def dore_to_dore(request):
    context ={}
    try:
        return render(request, 'services/dore_to_dore_pick_up.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')

def old_cloth(request):
    context ={}
    try:
        return render(request, 'services/old_cloth.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request)) 


def plastic(request):
    context ={}
    try:
        return render(request, 'services/plastic.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request)) 


def papers(request):
    context ={}
    try:
        return render(request, 'services/paper.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request)) 

def price_list(request):
    context ={}
    try:
        return render(request, 'pricelist.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request)) 

def contact(request):
    context ={}
    try:
        return render(request, 'contact.html')
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
        return render(request, 'cluster/cluster_dashboard.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
    
def New_customer(request):
    context ={}
    try:
        return render(request, 'cluster/add_customers.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))