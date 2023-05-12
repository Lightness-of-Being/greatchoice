from django import forms
from .models import Category,Product,Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title','content','photo',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title','content','photo',)
