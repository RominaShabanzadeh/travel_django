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