from .models import Profile,Post, Review, RATE_CHOICES
from django import forms

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username','bio','contact','avatar']

class PostModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3} ))
    location = forms.CharField(label = 'Your location')

    class Meta:
        model = Post
        fields = ['project_name','description','url','image','location',]  

class RateForm(forms.ModelForm):
    design = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
    usability = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
    content = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
    
    class Meta:
        model = Review
        fields=['design','usability','content','comment'] 