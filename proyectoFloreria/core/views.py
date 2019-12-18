from django.shortcuts import render
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
from .clase import elemento


#rest_framework
from rest_framework import viewsets
##from .serializers import FloreriaSerializer

# Create your views here.
#---CARRITOS---#


@login_required(login_url='/ingresar/')
def carrito(request):
    x=request.session["carritox"]
    suma=0
    for item in x:
        suma=suma+int(item["total"])
    return render(request,"core/carrito.html",{'x':x,'total':suma})   




@login_required(login_url='/ingresar/')
def carro_compras(request,id):
    f=Flor.objects.get(name=id)
    x=request.session["carritox"]
    el=elemento(1,f.name,f.precio,1)
    sw=0
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            sw=1
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    if sw==0:
        clon.append(el.toString())
    x=clon    
    request.session["carritox"]=x
    flors=Flor.objects.all()    
    return render(request,'core/galeria.html',{'flores':flors,'total':suma})

@login_required(login_url='/ingresar/')
def grabar_carro(request):
    x=request.session["carritox"]    
    usuario=request.user.username
    suma=0
    try:
        for item in x:        
            titulo=item["nombre"]
            precio=int(item["precio"])
            cantidad=int(item["cantidad"])
            total=int(item["total"])        
            boleta=Boleta(
                usuario=usuario,
                titulo=titulo,
                precio=precio,
                cantidad=cantidad,
                total=total,
                fecha=datetime.date.today()
            )
            boleta.save()
            suma=suma+int(total)  
            print("reg grabado")                 
        mensaje="Grabado"
        request.session["carritox"] = []
    except:
        mensaje="error al grabar"            
    return render(request,'core/carrito.html',{'x':x,'total':suma,'mensaje':mensaje})

@login_required(login_url='/ingresar/')
def carro_compras_mas(request,id):
    f=Flor.objects.get(name=id)
    x=request.session["carritox"]
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]        
    return render(request,'core/carrito.html',{'x':x,'total':suma})

@login_required(login_url='/ingresar/')
def carro_compras_menos(request,id):
    f=Flor.objects.get(name=id)
    x=request.session["carritox"]
    clon=[]
    suma=0
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)-1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]    
    return render(request,'core/carrito.html',{'x':x,'total':suma})    
@login_required(login_url='/ingresar/')
def vacio_carrito(request):
    request.session["carro"]=""
    x=request.session.get("carro","")
    return render(request,"core/carrito.html",{'x':x})

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#metodo de login LOGIN ACCESO
def login_acceso(request):
    
    #si alguien ha enviado algun dato
    if  request.POST:

        #se recuperan lso datos enviados
        usuario=request.POST.get("txtUsuario")
        password=request.POST.get("txtPassword")

        #creamos un modelo de usuarios para autentificar (con usuario y password)
        us= authenticate(request,username=usuario,password=password)
        msg=''
        request.session["carritox"] = []
        request.session["carrito"] = []

        #si el usuario existe y esta activo
        if us is not None and us.is_active:
            #autentifique el login yt pase el usuario
            auth_login(request,us)
            #te lleva al index
            return render(request,"core/index.html",{'msg':'CORRECTO'})
    #si no esta te lleva al login        
    return render(request,"core/ingresar.html",{'msg':'ERROR'})

#metodo cerrar sesion    
def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>alert('Sesion cerrada');window.location.href='/';</script>")




#se define el index como metodo de solicitud/peticion
def index (request):
    #se retorna una redireccion dela solicitud hacia index.html(te lleva a index)
    return render(request,'core/index.html')

@login_required(login_url='/ingresar/')
#se defien carrito registrado
def carritoregistrado (request):
    #se retorna una redireccion dela solicitud hacia index.html(te lleva a index)
    return render(request,'core/carritoregistrado.html')


#se define el galeria como metodo de solicitud/peticion
def galeria(request):
    flores=Flor.objects.all()
     #se retorna una redireccion dela solicitud hacia galeria.html(te lleva a galeria)
    return render(request,'core/galeria.html',{'lista':flores})    


#se define el quienes como metodo de solicitud/peticion
def quienes(request):
     #se retorna una redireccion dela solicitud hacia quienes.html(te lleva a quienes)
    return render(request,'core/quienes.html')    


#se define el ubcacio como metodo de solicitud/peticion
def ubicacion(request):
     #se retorna una redireccion dela solicitud hacia ubicacion.html(te lleva a ubicacion)
    return render(request,'core/ubicacion.html')    

    


#se define el registrarse como metodo de solicitud/peticion
def registrarse(request):
     #se retorna una redireccion dela solicitud hacia ubicacion.html(te lleva a ubicacion)
    return render(request,'core/registrarse.html') 

#se define el registrarse como metodo de solicitud/peticion
def ingresar(request):
     #se retorna una redireccion dela solicitud hacia ubicacion.html(te lleva a ubicacion)
    return render(request,'core/ingresar.html')         


@login_required(login_url='/ingresar/')
#Aca se hacen los metodos y eso#
#se define el formualrio como metodo de solicitud/peticion
def formulario(request):
  #se retorna una redireccion dela solicitud hacia formulario.html(te lleva a formulario)
    categorias=categoria.objects.all() # select * from Categoria
    if request.POST:
        # recuperar el valor del boton accion
        accion=request.POST.get("accion")
        if accion=='Guardar':            
            nombre=request.POST.get("txtNombre")
            precio=request.POST.get("txtPrecio")
            descrip=request.POST.get("txtDescripcion")
            imagen=request.FILES.get("txtImagen")
            catego=request.POST.get("cboCategoria")
            obj_categoria=categoria.objects.get(name=catego)

            #instanciar un objeto (modelo)
            florsita=Flor(
                name=nombre,
                precio=precio,
                descripcion=descrip,
                imagen=imagen,
                categoria=obj_categoria
            )

            florsita.save() #graba los datos del modelo
            return render(request,'core/formulario.html',{'listacategoria':categorias,'msg':'grabo'})



        if accion=='Eliminar':
            nombre=request.POST.get("txtNombre")#recupera el nombre y se borra por este
            florsita=Flor.objects.get(name=nombre)# lo busca entre las flores
            florsita.delete()#elimina          
            return render(request,'core/formulario.html',{'listacategoria':categorias,'msg':'elimino'})

    return render(request,'core/formulario.html',{'listacategoria':categorias})     

#####################################################################
def isset(variable):
	return variable in locals() or variable in globals()        

#class FloreriaViewset(ViewSet.ModelViewSet):
#    queryset = Pelicula.objectws.all()
#    serializer_class = FloreriaSerializer

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"