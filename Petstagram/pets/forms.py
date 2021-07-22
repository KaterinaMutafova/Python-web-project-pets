from django import forms

from Petstagram.pets.choices import TYPE_CHOICES
from Petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet

        labels = {
            'type': ('Type'),
            'name': ('Name'),
            'age': ('Age'),
            'description': ('Description'),
            'image': ('Image'),

        }
        widgets = {
            'type': forms.Select(choices=TYPE_CHOICES, attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),


        }

        fields = '__all__'

        # type = forms.ChoiceField(widget=forms.Select(choices=TYPE_CHOICES, attrs={"class": "form-control"}))
        # name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
        # age = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
        # description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
        # image = forms.ImageField(widget=forms.FileInput(attrs={"class": 'custom-file-input'}))


class EditPetForm(PetForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(attrs={"class": "form-control", 'readonly': True}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'custom-'}),

        }


