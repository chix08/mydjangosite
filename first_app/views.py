# from django.shortcuts import render
# from first_app.models import  AccessRecord
# 
# 
# # Create your views here.
# 
# def home(request):
#     web_list = AccessRecord.objects.order_by('date')
#     web_dict = {'access_record ': web_list}
#  #   my_dict = {"var": "Template", "num": "123"}
# 
#     return render(request, 'first_app/data.html', web_dict)

from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)


def home(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'first_app/data.html',date_dict)