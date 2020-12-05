# DRF Imports
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import loader
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR)

# Model Imports
from rank_app.models import Details

# Form Imports
from .forms import PostForm

def DetailView(request):
    form_class = PostForm()
    if request.method == "POST":
        form_class = PostForm(request.POST)
        if form_class.is_valid():
            objs = form_class.save()
            obj = Details.objects.filter(id=objs.id).values('rank')
            obj1 = Details.objects.filter(id=objs.id).values('name')
            return render(request, 'display.html', {'rank': obj, 'name':obj1})
        else:
            print("ERROR FORM INVALID")
    return render(request, "homepage.html",{"form":form_class})

 
#def RankView(request):
    #if request.method == "post":
        #uuid = request.GET.get('uuid')
        #rank = Details.objects.filter(uuid=uuid).values('rank').first()
        #return render(request, "display.html",{"rank": rank})
    #else:
        #print("ERROR FROM INVALID")
    return render(request, "checkrank.html")
    