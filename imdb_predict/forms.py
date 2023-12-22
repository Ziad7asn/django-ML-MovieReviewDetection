from django import forms
from .models import File
from django.core.validators import FileExtensionValidator

csv_file = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}))
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        file = forms.ImageField(validators=[FileExtensionValidator('csv')])
        fields=('file_name','file')

