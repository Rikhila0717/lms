from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

def path_and_rename(instance,filename):
    upload_to = 'Images/'

    #extension
    ext = filename.split('.')[-1]
    #get filename
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username,ext)
    return os.path.join(upload_to, filename)


#user model
class User_Profile(models.Model):

    #one-to-one relationship for the user
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #models.cascade, that is on the deletion of that user all the model info related to that user will be deleted

    bio = models.CharField(max_length=150,blank=True)
    #biopic can be left blank

    profile_pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture", blank=True)
    #profile pic can be left blank

    #types of users available
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = models.CharField(max_length=10, choices= user_types,default=student)

    def __str__(self):
        return self.user.username
