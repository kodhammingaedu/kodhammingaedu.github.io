from django import forms
from django.contrib import admin
from .models import Car, Color

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'colors': forms.CheckboxSelectMultiple,
        }


class CarAdmin(admin.ModelAdmin):
    form = CarForm

admin.site.register(Car)
admin.site.register(Color)

admin.site.site_header = 'Toyota Site Admin'