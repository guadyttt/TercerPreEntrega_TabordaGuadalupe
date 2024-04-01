from django import forms
from . models import *
from . models import Alumno
from . models import Profesor


class Curso_formulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    comision=forms.IntegerField()
    
    
class AlumnoForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    comision=forms.IntegerField()
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

    def save(self, commit=True):
        alumno = super().save(commit=False)
        
        if commit:
            alumno.save()
        return alumno
    
    
class ProfesorForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    comision=forms.IntegerField()
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

    def save(self, commit=True):
        profesor = super().save(commit=False)
        
        if commit:
            profesor.save()
        return profesor