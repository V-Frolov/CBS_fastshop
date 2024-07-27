from django import forms
from .models import Review, Order


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product']
        # widgets = {
        #     'product': forms.CheckboxSelectMultiple(),
        # }
