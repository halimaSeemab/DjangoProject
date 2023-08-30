from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import list, LM, WH



def options(request):
  template = loader.get_template("options.html")
  return HttpResponse(template.render())


def myfirst(request):
  template = loader.get_template("myfirst.html")
  return HttpResponse(template.render())




def contactus(request):
  template = loader.get_template("contactus.html")
  return HttpResponse(template.render())









def lists(request):
  mybooks = list.objects.all().values()
  lm = LM.objects.all().values()
  wh = WH.objects.all().values()
  template = loader.get_template('list.html')
  context = {
    'mybooks': mybooks,
    'lm': lm,
    'wh': wh
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mybooks = list.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mybooks': mybooks,
  }
  return HttpResponse(template.render(context, request))



def details2(request, id):
  lm = LM.objects.get(id=id)
  template = loader.get_template('details2.html')
  context = {
    'lm': lm,
  }
  return HttpResponse(template.render(context, request))






def details4(request, id):
  wh = WH.objects.get(id=id)
  template = loader.get_template('details4.html')
  context = {
    'wh': wh,
  }
  return HttpResponse(template.render(context,request))







