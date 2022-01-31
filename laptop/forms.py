from django import forms

from laptop.models import Laptop, Gadget


class LaptopCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('brand', 'name', 'GPU', 'graphics_card', 'RAM',
                  'memory', 'display', 'date', 'price')


class GadgetCreateUpdateForm(forms.Form):
    class Meta:
        model = Gadget
        fields = ('brand', 'name', 'price')