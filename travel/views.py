from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render



from travel.forms import travel_frm
from travel.models import travel_mdl


def index(request):
    travels=travel_mdl.objects.all()
    return render(request,'index.html',{'travels':travels})

def create_travel(request):
    form=travel_frm()
    if request.method=="POST":
        form=travel_frm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'register_travel.html',{'form':form})

def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'registration/register.html',{'form':form})