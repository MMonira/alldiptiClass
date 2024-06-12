from django.shortcuts import render , redirect , get_object_or_404
from backendapp.models import *
from backendapp.forms import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages





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
         return redirect('dashboard')
   else:
      form = customAuthForm()
      
   return render(request,'signin.html',{'form':form})


@login_required
def logup(request):
   logout(request)
   return redirect('signin')



@login_required
def dashboard(request):
   return render(request,'dashboard.html')


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
   
   jobdict = {
      'info': jobmodels,
   }
   already_applied = jobApplyModel.objects.filter(applicants = applicant , jobmodel = jobmodels).exists()
   
   # if already_applied:
   #    messages.success(request, 'You already applied')
   #    return redirect('joblist')

   
   if request.method == 'POST':
      form = applyJobForm(request.POST , request.FILES)
      if form.is_valid():
         f = form.save(commit=False)
         f.applicants = applicant
         f.jobmodel = jobmodels
         f.save()
         return redirect('joblist')
   else:
      form = applyJobForm()
      jobdict['form'] = form
   # jobdict['already_applied'] = already_applied
   
   return render(request, 'seeker/applyjob.html', jobdict)


