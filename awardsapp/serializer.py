from rest_framework import serializers
from awardsapp.models import Post,Profile

        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','project_name','description','author')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','username','bio')