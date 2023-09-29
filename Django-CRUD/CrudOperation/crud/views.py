from django.shortcuts import render,redirect
from .forms import FormTache
from .models import Tache


# Create your views here.

def index(request):
    form = FormTache(request.POST or None)
    if form.is_valid():
        form.save()
        form = FormTache()
        
    liste_taches = Tache.objects.all()
    context = {
        'form':form,
        'taches':liste_taches
    }
    
    return render(request,'index.html',context)

def modifier(request,myId):
    obj = Tache.objects.get(id=myId)
    form = FormTache(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'modifier.html',{'form':form})

def supprimer(request,myId):
    obj = Tache.objects.get(id=myId)
    obj.delete()
    return redirect('/')
        
        
    
    
