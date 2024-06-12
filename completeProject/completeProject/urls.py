
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('backendapp.urls')),
    path('',signin, name='signin'),
    path('signup/',signup, name='signup'),
    path('dashboard/',dashboard, name='dashboard'),
    path('addjob/',addjob, name='addjob'),
    path('joblist/',joblist, name='joblist'),
    
    
    path('profile/',profile, name='profile'),
    path('appliedjob/',appliedjob, name='appliedjob'),
    path('postedjob/',postedjob, name='postedjob'),
    path('applicants/<int:myid>',applicants, name='applicants'),
    path('logup/',logup, name='logup'),
    
    
    
    path('editjob/<str:myid>',editjob, name='editjob'),
    path('deletejob/<str:myid>',deletejob, name='deletejob'),
    path('apply/<str:myid>',apply, name='apply'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
