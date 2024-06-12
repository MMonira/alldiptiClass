from django.shortcuts import render , redirect
from . sforms import CreateuserForm

def homepage(request):
   return render(request,'backendapp/index.html')

   
def register(request):
   
   form = CreateuserForm()

   if request.method == 'POST':
      form = CreateuserForm(request.POST)

      if form.is_valid():
         form.save()
         
         return redirect('my_login')
   context = {'registerform': form}
   
   return render(request,'backendapp/register.html', context=context)


def my_login(request):
   return render(request,'backendapp/my_login.html')


def dashboard(request):
   return render(request,'backendapp/dashboard.html')
