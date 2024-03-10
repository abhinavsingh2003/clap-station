from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.
# from django.contrib.auth.models import AbstractUser
# from .manager import  UserManager


# Create your models here.



def validate_image_dimensions(value):
    max_height = 360
    max_width = 800

    with Image.open(value) as img:
        width, height = img.size

    if width > max_width or height > max_height:
        raise ValidationError(f"Image dimensions must be at most {max_width}x{max_height} pixels.")



    
# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     user_bio = models.CharField(max_length=100)
#     user_profile_image = models.ImageField(upload_to="profile_image")

#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []

#     # Unique names for related fields to avoid clashes
#     liked_posts = models.ManyToManyField('clapStationWebsite.posts', default=None, blank=True, related_name='liked_users')
#     user_permissions_custom = models.ManyToManyField('auth.Permission', verbose_name='user_permissions', blank=True,
#                                                      related_name='user_set_custom')
#     groups_custom = models.ManyToManyField('auth.Group', verbose_name='groups', blank=True, related_name='user_set_custom')

#     def __str__(self):
#         return self.username






class posts(models.Model):
    img = models.ImageField(upload_to= "posts/image", default="", help_text=" ClapStation upload image | height: 360px | width: 640px"
                            , validators=[validate_image_dimensions])
    about = models.CharField(max_length = 250 )
    liked =models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    updated=models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add = True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    
    def __str__(self):
        return str(self.about)


    @property
    def num_likes(self):
        return self.liked.all().count()



LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(posts,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)
    

class Event_detail_page(models.Model):
    eventname = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/' )


    def __str__(self):
        return str(self.eventname)




class advertisements(models.Model):
    img = models.ImageField(upload_to="advertisement/image",default="")
    created_at = models.DateTimeField(auto_now_add = True )

class upComingEvents(models.Model):
    img = models.ImageField(upload_to="upcoming/image", default="")
    phone= models.CharField(max_length=10)
    email= models.EmailField(max_length=50)
    address=models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True )




class user_details(models.Model):
    img = models.ImageField(upload_to="profile/image", default="")
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add = True)

# create group
class Create_group(models.Model):
    image = models.ImageField(upload_to="creategroup/image",default="",null=True, blank=True)
    groupname=models.CharField(max_length=20)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.groupname)


class Signup(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    mobile_email = models.CharField( max_length=50)
    day= models.IntegerField()
    month= models.CharField(max_length=20)
    year= models.IntegerField()
    role = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

class Contact_us(models.Model):
    First_N = models.CharField(max_length=50)
    Last_N = models.CharField(max_length=50)
    mobileno = models.IntegerField()
    emailid = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self)->str:
        return f"{self.First_N} - {self.Last_N} - {self.emailid}"