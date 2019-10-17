from django.shortcuts import render
from django.http import HttpResponseRedirect
from WebApp import  forms
from WebApp.models import BatchTiming,Assignment,notification

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact_us(request):
    return render(request,'contact_us.html')

def gallery(request):
    return render(request,'gallery.html')

def batch_timing(request):
    return render(request,'batch_timing.html')


def signup(request):
    form=forms.StdForm()
    if request.method=='POST':
        form=forms.StdForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/byee')
    else:
        form=forms.StdForm()
    return render(request,'signup.html',{'form':form})


def thanks(request):
    return render(request,'thanks.html')

def welcome_to_AEC(request):
    return render(request,'welcome_to_AEC.html')



def Batch_Time_View(request):
	BT_List=BatchTiming.objects.all()
	My_Dict={'list':BT_List }
	return render(request,'batch_timing.html',My_Dict)


def assignment_View(request):
    A_List=Assignment.objects.all()
    mydict={'list':A_List}
    return render(request,'assignment.html',context=mydict)

def notification_View(request):
    N_list=notification.objects.all()
    mydict={'list':N_list}
    return render(request,'notification.html',mydict)
