from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
        def min_length_check(val):
            if len(val) <= 10:
                raise  ValidationError("Value must be greater than 10")

        title = models.CharField(validators=[min_length_check], max_length=255)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        objects =models.Manager

        def __str__(self):
            return self.title

        class Meta:
            db_table = 'categories'
            verbose_name='Category'
            verbose_name_plural='Categories'
            ordering=['-created_at']

class Posts(models.Model):
        def min_length_check(val):
            if len(val) <= 10:
                raise  ValidationError("Value must be greater than 10")

        title = models.CharField(validators=[min_length_check], max_length=255)
        user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
        category=models.ManyToManyField(Category,related_name='categories',default=0)
        content = models.TextField(validators=[validators.validate_integer])
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        objects =models.Manager

        def __str__(self):
            return self.title
        class Meta:
            db_table = 'posts'
            verbose_name='Post'
            verbose_name_plural='Posts'

class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields =['title','content','user','category']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Post title"}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'})

        }
        help_texts={
            'title':'Enter Title here'
        }
        error_messages={}
        labels={
            'title':'Enter Post Title'
        }

def clean(self):
    fields = self.cleaned_data
    keys = list(fields.keys())
    if(len(fields['title']) <=10):
        raise validators.ValidationError("%(val)s Must be Greater than 10",params={'val':key[0]})
    if(len(fields['title']) <=10):
        raise validators.ValidationError("%(val)s Must be Greater than 10",params={'val':key[1]})