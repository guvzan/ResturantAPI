from django import forms

from .models import Resturant, Menu

class ResturantForm(forms.ModelForm):
    class Meta:
        model = Resturant
        fields = ['name', 'password', 'active_menu']
        labels = {
            'name': 'Resturant name',
            'password': 'Password',
            'active_menu': 'Active menu'
        }


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['main', 'salad', 'dessert', 'drink', 'for_day', 'resturant']
        labels = {
            'main': 'Main dish',
            'salad': 'Salad',
            'dessert': 'Dessert',
            'drink': 'Drink',
            'for_day': 'Day of week (number 1-7)',
            'resturant': 'Resturant'
        }