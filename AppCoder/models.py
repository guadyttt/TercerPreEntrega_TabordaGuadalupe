from django.db import models



class Curso (models.Model):
    nombre= models.CharField(max_length=40)
    comision=models.IntegerField()
    
    
class Alumno (models.Model):
    nombre= models.CharField(max_length=40)
    comision=models.IntegerField()
    
    
    
class Profesor(models.Model):
    nombre= models.CharField(max_length=40)
    comision=models.IntegerField()   