from django.shortcuts import render


# Create your views here.
def temptest(request):

    return render(request, 'lecfourapp/testtemplate.html')
