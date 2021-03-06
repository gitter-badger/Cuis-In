#-*- coding: utf-8 -*-
from django import forms
from recipe.models import Recipe
import floppyforms


def get_categories():
    return ('1', 'Option 1'), ('2', 'Option 2')


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = {'slug'}
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'note': floppyforms.RangeInput(attrs={'min': 0, 'max': 5}),
            'hard': floppyforms.RangeInput(attrs={'min': 0, 'max': 5}),
            'cuissonTime': floppyforms.NumberInput(attrs={'min': 0}),
            'preparationTime': floppyforms.NumberInput(attrs={'min': 0}),
            'serves': floppyforms.NumberInput(attrs={'min': 0}),
        }
