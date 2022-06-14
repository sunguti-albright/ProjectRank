from django.test import TestCase
from .models import Profile,Post, Review
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        user = User.objects.create()
        self.new_profile = Profile(user = user,bio = 'test_bio',created = '2022-06-14')
        self.new_profile.save()
        def test_instance(self):
            self.assertTrue(isinstance(self.new_profile,Profile)) 


class PhotoTestClass(TestCase):
        def setUp(self):
            user = User.objects.create()


            self.new_project = Post(project_name ='test_project_name',description = 'test_description',url = 'test_url',location = 'test_location',created = '2022-06-14',author = user )

        def test_instance(self):
            self.assertTrue(isinstance(self.new_project,Post))   

        def test_save_method(self):
            self.new_project.save_project()
            project = Post.objects.all()
            self.assertTrue(len(project) > 0)    

        def tearDown(self):
            Post.objects.all().delete()
            Profile.objects.all().delete()

        def test_delete_method(self):
            self.new_project.save_project()
            self.new_project.delete_project()
            project = Post.objects.all()
            self.assertTrue(len(project) == 0)    

        def test_update_method(self):
            self.new_project.save_project()
            self.new_project.update_project()
            project = Post.objects.all()
            self.assertTrue(len(project) > 0) 

        def test_get_project_by_id(self):
            id = Post.get_project_by_id()
            self.assertTrue(len(id) == 0)    


class ReviewTestCases(TestCase):
    def setUp(self):      
        self.new_review = Review(id=1,user='Jid',project='Instagram',design='1',usability='1',content='1',overall='1',comment='comment')
        self.new_review.save_review()
        
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))
                