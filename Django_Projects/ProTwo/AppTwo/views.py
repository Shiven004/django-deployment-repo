from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import AccessRecord,WebPage,Topic


# Create your views here.
def index(request):
    #my_dict = {'insert_me':"Hello!! I am from views.py.index fn some text"}
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'index.html',context=date_dict)

def help(request):
    my_help ={'help_me': "Hello!! I am from views.py for Help Page"}
    return render(request,'help.html',context=my_help)
