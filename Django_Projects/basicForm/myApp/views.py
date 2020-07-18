from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'myApp/index.html')

def form_name_view(request):
    form = forms.FormName()
    #check if request is post
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something
            print("************ Form validation successful,print in console! ****************")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request,'myApp/form_name.html',{'form':form})
