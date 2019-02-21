from django.shortcuts import render


# Create your views here.

def home(request) :
    my_dict = {"var" : "Template" , "num" : "123"}
    return render(request , 'first_app/temp.html' , my_dict)
