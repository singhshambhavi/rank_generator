# DRF Imports
from django.shortcuts import render
from rest_framework.response import Response
from django.template import loader


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

 
