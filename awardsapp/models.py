from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length = 255,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(default='no bio',max_length=300)
    contact = models.IntegerField(default=0)
    avatar = models.ImageField(default='avatar.jpg',upload_to = 'avatars/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.created}'

class Post(models.Model):
    project_name = models.CharField(max_length = 255)
    description = models.TextField()
    url = models.URLField(unique=True)
    image = models.ImageField(upload_to = 'posts',validators = [FileExtensionValidator(['png','jpg','jpeg'])])
    location = models.CharField(max_length = 255)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return str(self.description[:20])

    def save_project(self):
        self.save() 

    def delete_project(self):
        self.delete()  

    def  update_project(self):
        self.save()  

    @classmethod
    def get_project_by_id(cls,id=None):
        photos = cls.objects.filter(id = id)   
        return photos     
        
    @classmethod
    def search_by_project_name(cls,search_term):
        project = cls.objects.filter(project_name__icontains = search_term)   
        # We filter the model data using the __icontains query filter
        return project     

    class Meta:
        ordering = ['-created'] 

#product review model
RATE_CHOICES = [
	(1,'1 - Unsatisfactory'),
	(2,'2 - Pathetic'),
	(3,'3 - Very bad'),
	(4,'4 - Bad'),
	(5,'5 - Average'),
	(6,'6 - Okay'),
	(7,'7 - Good'),
	(8,'8 - Very Good'),
	(9,'9 - Excellent'),
	(10, '10 - Perfect'), 
]
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Post, on_delete = models.CASCADE)
    design = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=5) 
    usability =models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=5)  
    content = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=5)
    comment = models.CharField(max_length=250, blank=True,default='')  
    overall = models.IntegerField(blank=True,default=0)   