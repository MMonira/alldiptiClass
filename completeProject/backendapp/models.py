from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
   USER = [
      ('user','User'),
      ('admin','Admin'),
   ]
   
   user_type = models.CharField(max_length=100, choices=USER , null=True)
   profile_pic = models.ImageField (upload_to='static/media', null=True)
   age = models.CharField(max_length=30 , null=True)
   city = models.CharField(max_length=100, null=True)

class CategoryModel(models.Model):
   user = models.ForeignKey(Custom_user, on_delete=models.CASCADE , null=True)
   category = models.CharField(max_length=100 , null=True)

class TasknameModel(models.Model):
   category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE , null=True)
   create_at = models.DateField(auto_now=True, null=True)
   complete_at = models.DateField( null=True)
   status = models.CharField(max_length=100, default='On going',null=True)
   due_date = models.DateField(null=True)
   update_at = models.DateField(auto_now_add=True, null=True)
   taskName = models.CharField(max_length=100, null=True)
   description = models.TextField(null=True)
   
class secondCustomUser(models.Model):
   username = models.CharField(max_length=100 , null=True)
   email = models.CharField(max_length=100 , null=True)
   first_name = models.CharField(max_length=100 , null=True)
   password = models.CharField(max_length=100 , null=True)
   
   
class Post(models.Model):
   title = models.CharField(max_length=75)
   body = models.TextField()
   slug = models.TextField()
   date = models.DateTimeField(auto_now_add=True)
   banner = models.ImageField(default='fallback.png', blank=True)

   def __str__(self):
      return self.title
      
class RecruiterModel(models.Model):
   user = models.OneToOneField(Custom_user , on_delete=models.CASCADE , related_name='recruitermodel')
   company_name = models.CharField(max_length=100)
   company_location = models.CharField(max_length=100)
   company_logo = models.ImageField(upload_to='static/media')

   def __str__(self):
      return f'{self.user} {self.user.email} {self.company_name}'
   
class JobseekerModel(models.Model):
   username = models.OneToOneField(Custom_user , on_delete=models.CASCADE, related_name='seekermodel')
   qualification = models.TextField()
   experience = models.CharField(max_length=50)
   skills = models.CharField(max_length=50)
   resume = models.FileField(upload_to='static/media')
   
   def __str__(self) :
      return self.username.username + ' ' + self.experience


class JobModel(models.Model):
    job_title=models.CharField(max_length=100)
    qualifications=models.CharField(max_length=100)
    deadline=models.DateField()
    salary=models.CharField(max_length=100)
    number_of_openings = models.IntegerField(null=True)
    CATE = [
      ('education','Education'),
      ('Medical','Medical'),
      ('Design','Design'),
      ('Developer','Developer'),
    ]
    category = models.CharField(choices=CATE, max_length=40 , null=True)
    job_description = models.TextField(null=True)
    skills = models.CharField(max_length=100, null=True)
    created_by=models.ForeignKey(Custom_user,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.created_by.username + ' ' + self.job_title
     
     
class jobApplyModel(models.Model):
   applicants = models.ForeignKey(Custom_user, on_delete=models.CASCADE , related_name='applients')
   jobmodel = models.ForeignKey(JobModel, on_delete=models.CASCADE)
   skills=models.CharField(max_length=100)
   resume = models.FileField(upload_to='media/seeker_resume')
   seeker_profile_pic = models.ImageField(upload_to='media/seeker_profile_pic')
   qualifications = models.TextField()
   status=models.CharField(max_length=100, default="Pending")
   date_fix=models.DateField(null=True)
   def __str__(self):
      return self.applicants.username