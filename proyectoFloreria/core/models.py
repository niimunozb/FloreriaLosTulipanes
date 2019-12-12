from django.db import models





# Create your models here.
class categoria(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    calificacion=models.IntegerField()

    def __str__(self):
        return self.name




class Flor(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    precio=models.IntegerField()
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to='',null=True)
    categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
