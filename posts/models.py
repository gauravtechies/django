from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
# Create your models here.


class Posts(models.Model):
        def min_length_check(val):
            if len(val) <= 10:
                raise  ValidationError("Value must be greater than 10")

        title = models.CharField(validators=[min_length_check], max_length=255)
        content = models.TextField(validators=[validators.validate_integer])
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        objects =models.Manager

        def __str__(self):
            return self.title



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

class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields =['title','content']


def clean(self):
    fields = self.cleaned_data
    keys = list(fields.keys())
    if(len(fields['title']) <=10):
        raise validators.ValidationError("%(val)s Must be Greater than 10",params={'val':key[0]})
    if(len(fields['title']) <=10):
        raise validators.ValidationError("%(val)s Must be Greater than 10",params={'val':key[1]})