from django.contrib import admin
from .models import *

class customUserDisplay(admin.ModelAdmin):
   list_display = ['username','email', 'first_name', 'city' ,'user_type']
   search_fields = ['username','email', 'first_name', 'city']
   fieldsets = [
      (
         'Welcom to our site its a title',
         { 'fields':['username','email', ('first_name', 'last_name') , 'city']}
      ),
      (
         'Advanced Option',
         {
            'fields': ['user_type','profile_pic']
         }
      )
   ]


admin.site.register(Custom_user, customUserDisplay)
admin.site.register(CategoryModel)
admin.site.register(TasknameModel)
admin.site.register(secondCustomUser)
admin.site.register(Post)
admin.site.register(RecruiterModel)
admin.site.register(JobseekerModel)
admin.site.register(JobModel)
admin.site.register(jobApplyModel)

