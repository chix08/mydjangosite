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
from first_app.models import Topic, AccessRecord
from . import forms as f


# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)


def home(request):
    tp = Topic()
    webpages_list = tp.__str__()
    webpages_list_two = AccessRecord.objects.order_by('date')
    # print(webpages_list_two)
    # what is objects here doing and if i call the str function
    # then y it is not visible
    date_dict = {"access_records": webpages_list_two}
    return render(request, 'first_app/data.html', date_dict)


def formtest(request):
    form = f.NameForm()
    if request.method == 'POST':
        form = f.NameForm(request.POST)
        if form.is_valid():
            print("Validation Success")
            print(form.cleaned_data['your_name'])
        print('*' * 10)
        data = form.cleaned_data.get("form_field")
        print(data)
    name_dir = {'user': form}

    return render(request, 'first_app/theform.html', name_dir)
