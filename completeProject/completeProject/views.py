from django.shortcuts import render , redirect , get_object_or_404
from backendapp.models import *
from backendapp.forms import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from datetime import date




def signup(request):
   if request.method == 'POST':
      form = CustomUserForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         
         return redirect('signin')
   else:
      form = CustomUserForm()
   return render(request,'signup.html',{'form':form})


   

def signin(request):
   if request.method == 'POST':
      form = customAuthForm(request, data = request.POST)

      if form.is_valid():
         f = form.get_user()
         login(request,f)
         return redirect('joblist')
   else:
      form = customAuthForm()
      
   return render(request,'signin.html',{'form':form})


@login_required
def logup(request):
   logout(request)
   return redirect('signin')



@login_required
def dashboard(request):
   search =request.GET.get('search')
   # jobs = JobModel.objects.filter(job_title = search)
   jobs = JobModel.objects.filter(
      Q(job_title__icontains= search)|
      Q(salary__icontains = search)|
      Q(created_by__username__icontains = search)
      )
   job_filtered = []

   for i in jobs:
      already_applied = jobApplyModel.objects.filter(applicants = request.user , jobmodel = i).exists()
      job_filtered.append(
         (i, already_applied),
      )

      context = {
         'already_applied':already_applied,
         'job_filtered': job_filtered
      }
   return render(request,'dashboard.html', context)


@login_required
def addjob(request):
   if request.method == 'POST':
      form = jobAddform(request.POST , request.FILES)
      cuUser = request.user
      
      if form.is_valid():
         f = form.save(commit=False)
         f.created_by = cuUser
         f.save()
         return redirect('joblist')
   else:
      form = jobAddform()
      
   return render(request,'recruiter/addjob.html',{'form':form})

   

@login_required
def joblist(request):
   dataobjs = JobModel.objects.all()
   job_filtered = []

   for dataobj in dataobjs:
      already_applied = jobApplyModel.objects.filter(applicants = request.user , jobmodel = dataobj).filter()
      job_filtered.append(
         (dataobj , already_applied),
      )
   context = {
      'job_filtered':job_filtered
   }
   return render(request,'joblist.html',context)

@login_required
def profile(request):
   
   return render(request,'profile.html')


@login_required
def appliedjob(request):
   applied_job = jobApplyModel.objects.filter(applicants = request.user)

   return render(request,'seeker/appliedjob.html', {'applied_job':applied_job})




@login_required
def postedjob(request):
   
   posted_job = JobModel.objects.filter(created_by = request.user)

   return render(request,'recruiter/postedjob.html', {'applied_job':posted_job})


@login_required
def applicants(request, myid):

   job = JobModel.objects.get(id = myid)

   applicants = jobApplyModel.objects.filter(jobmodel = job)

   context = {
      'applicants': applicants,
      'job': job,
   }
   
   return render(request,'recruiter/applicants.html', context)


   
   
@login_required
def editjob(request, myid):
   info = get_object_or_404(JobModel, id = myid)

   if request.method == 'POST':
      form = jobAddform(request.POST, instance=info)

      if form.is_valid():
         form.save()
         return redirect('joblist')
   else:
      form = jobAddform(instance=info)


   return render(request,'recruiter/editjob.html', {'form':form, 'info':info})


@login_required
def deletejob(request, myid):
   info = get_object_or_404(JobModel, id = myid)
   info.delete()
   return redirect('joblist')
   
@login_required
def apply(request, myid):
   applicant = request.user
   jobmodels = get_object_or_404(JobModel , id = myid)
   
   # jobdict = {
   #    'info': jobmodels,
   # }
   # already_applied = jobApplyModel.objects.filter(applicants = applicant , jobmodel = jobmodels).exists()
   
   # if already_applied:
   #    messages.success(request, 'You already applied')
   #    return redirect('joblist')

   
   if request.method == 'POST':
      form = applyJobForm(request.POST , request.FILES)
      print(form)
      if form.is_valid():
         print("hhsefjhsesgsgg")
         f = form.save(commit=False)
         f.applicants = applicant
         f.jobmodel = jobmodels
         f.save()
         return redirect('joblist')
   else:
      print("grndsfwged")
      form = applyJobForm()
      # jobdict['form'] = form
   # jobdict['already_applied'] = already_applied
   
   return render(request, 'seeker/applyjob.html', {'form':form})


@login_required
def addtask(request):
   category= CategoryModel.objects.all()
   
   if request.method == 'POST':
      taskname = request.POST.get('exampleInputEmail1')
      descrip = request.POST.get('exampleInputPassword1')
      duedate = request.POST.get('due_date')
      category = request.POST.get('category')
      catmodel = CategoryModel.objects.get(category = category)


   
      addData = TasknameModel(
         category = catmodel,
         taskName = taskname,
         description = descrip,
         due_date = duedate,
      )
      addData.save()
      return redirect('tasklist')

   return render(request,'recruiter/addtask.html',{'category':category})


@login_required

def tasklist(request):
   alltask = TasknameModel.objects.all()

   return render(request,'tasklist.html',{'tasks':alltask})
   

@login_required

def homepage(request):
   alltask = TasknameModel.objects.filter(due_date__gt = date.today())
   upcomingtask = TasknameModel.objects.filter(status = "On going").count()
   completedtask = TasknameModel.objects.filter(status = "Completed").count()


   return render(request,'homepage.html',{'tasks':alltask,'upcoming':upcomingtask,'completedC':completedtask})



