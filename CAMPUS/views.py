from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from CAMPUS.models import Job,Application

# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render(request,'index.html')

def signpage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password1')
        if pass1 !=pass2:
            return HttpResponse("your password is invalid")
        else: 
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')        
    return render(request,'signup.html')
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('Username and password is incorrect!!')

    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')  

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job_detail.html', {'job': job})

def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user.student
            application.job = job
            application.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()
    return render(request, 'apply_for_job.html', {'form': form, 'job': job})
def jnncepage(request):
    return HttpResponse('jannve')