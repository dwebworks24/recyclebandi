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