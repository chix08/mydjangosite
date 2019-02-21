from django.shortcuts import render


# Create your views here.

def home(request) :
    my_dict = {"var" : "Template"}
    return render(request , 'temp.html' , my_dict)
