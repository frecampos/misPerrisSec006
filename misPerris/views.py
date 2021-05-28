from django.contrib import auth
from django.shortcuts import render
# importar le modelo de tablas para trabajar
from .models import Categoria, Mascota, Galeria

# importar el modelo de la tabla User
from django.contrib.auth.models import User
# importar libreria para autentificar usuarios
from django.contrib.auth import authenticate,logout,login as login_aut
# importar una libreria decoradora que evita el ingreso a las paginas
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

def cerrar_sesion(request):
    logout(request)
    categorias = Categoria.objects.all()
    contexto={"cate":categorias}
    mascotas = Mascota.objects.filter(publicar=True).order_by('-nombre')[:3]
    contexto["mascotas"]=mascotas
    return render(request, "index.html",contexto)   

def login(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            categorias = Categoria.objects.all()
            contexto={"cate":categorias}
            return render(request, "index.html",contexto)
        else:
            mensaje="no existe usuario o contraseña incorrecta"
    contexto={"mensaje":mensaje}
    return render(request,"login.html",contexto)

def index(request):
    categorias = Categoria.objects.all()
    contexto={"cate":categorias}
    mascotas = Mascota.objects.filter(publicar=True).order_by('-nombre')[:3]
    contexto["mascotas"]=mascotas
    return render(request, "index.html",contexto)

def galeria(request):
    mascotas = Mascota.objects.filter(publicar=True)
    categorias = Categoria.objects.all()
    contexto = {"mascotas":mascotas,"categorias":categorias}
    return render(request, "galeria.html",contexto)

def filtro_categoria(request):
    mascotas = Mascota.objects.all() # select * from Mascota
    cant = Mascota.objects.all().count()
    categorias = Categoria.objects.all()
    if request.POST:
        cate = request.POST.get("cboCategoria")
        obj_categoria = Categoria.objects.get(nombre=cate)
        mascotas= Mascota.objects.filter(categoria=obj_categoria).filter(publicar=True)
        cant = Mascota.objects.filter(categoria=obj_categoria).filter(publicar=True).count()
        #mascotas = Mascota.objects.filter(categoria__pk=cate)
    contexto = {"mascotas":mascotas,"categorias":categorias,"cantidad":cant}
    return render(request, "galeria.html",contexto)

def filtro_cate(request,id):
    categorias = Categoria.objects.all()
    obj_categoria = Categoria.objects.get(nombre=id)
    mascotas= Mascota.objects.filter(categoria=obj_categoria).filter(publicar=True)
    cant = Mascota.objects.filter(categoria=obj_categoria).filter(publicar=True).count()
    #mascotas = Mascota.objects.filter(categoria__pk=cate)
    contexto = {"mascotas":mascotas,"categorias":categorias,"cantidad":cant}
    return render(request, "galeria.html",contexto)

def filtro_descripcion(request):
    mascotas = Mascota.objects.all() # select * from Mascota
    cant = Mascota.objects.all().count()
    categorias = Categoria.objects.all()
    if request.POST:
        texto = request.POST.get("txtDesc")
        mascotas= Mascota.objects.filter(descripcion__contains=texto).filter(publicar=True)
        cant = Mascota.objects.filter(descripcion__contains=texto).filter(publicar=True).count()
    contexto = {"mascotas":mascotas,"categorias":categorias,"cantidad":cant}
    return render(request, "galeria.html",contexto)

def formulario(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellidos = request.POST.get("txtApellidos")
        email = request.POST.get("txtEmail")
        nom_usuario = request.POST.get("txtUsuario")
        pass1 = request.POST.get("txtPass1")
        
        usu = User()
        usu.first_name = nombre
        usu.last_name = apellidos
        usu.email = email
        usu.username= nom_usuario
        usu.set_password(pass1)
        usu.save()

        mensaje="Grabo"
    contexto = {"mensaje":mensaje}
    return render(request, "formulario.html",contexto)

def contacto(request):
    return render(request, "contacto.html")

def quienes(request):
    return render(request, "quienes_somos.html")

def ficha(request, id):
    try:
        mascota= Mascota.objects.get(nombre=id)
        galeria = Galeria.objects.filter(mascota=mascota)
        contexto = {"mascota":mascota,"galeria":galeria}
        return render(request, "ficha.html",contexto)
    except:
        contexto ={"mensaje":"no existe mascota"}
        return render(request, "ficha.html",contexto)

def formvalida(request):
    return render(request, "formulario2.html")

@login_required(login_url='/login/')
@permission_required('misPerris.add_mascota',login_url='/login/')
def registro(request):
    categorias = Categoria.objects.all() # select * from Categoria
    mensaje=""
    usuario = request.user.username # nombre del usuario 
    if request.POST:
        nombre = request.POST.get("txtNombre")
        try:
            mas = Mascota.objects.get(nombre=nombre)
            mensaje ="nombre de mascota existe"
        except:
            edad = request.POST.get("txtEdad")
            desc = request.POST.get("txtDesc")
            cate = request.POST.get("cboCategoria")
            obj_cate = Categoria.objects.get(nombre=cate) # select * from Categoria where nombre=''
            imagen = request.FILES.get("txtImg")
            
            mas = Mascota()
            mas.nombre = nombre                
            mas.edad=edad
            mas.descripcion=desc

            if imagen is not None:
                mas.imagen= imagen
            
            mas.categoria=obj_cate
            mas.usuario = usuario
            
            mas.save()
            mensaje="grabo"

    mascotas = Mascota.objects.filter(usuario=usuario)  
    cant = Mascota.objects.filter(usuario=usuario).count()
    context = {"categorias":categorias,"mensaje":mensaje,"mascotas":mascotas}
    context["cantidad"]=cant
    return render(request, "registro.html",context)

@login_required(login_url='/login/')
@permission_required('misPerris.delete_mascota',login_url='/login/')
def eliminar(request, id):
    try:
        mas = Mascota.objects.get(nombre=id)
        mas.delete()
        mensaje ="elimino mascota"
    except:
        mensaje="no elimino mascota"

    mascotas = Mascota.objects.filter(usuario=request.user.username)  
    categorias= Categoria.objects.all()
    context = {"categorias":categorias,"mensaje":mensaje,"mascotas":mascotas}
    return render(request, "registro.html",context)

@login_required(login_url='/login/')
def buscar_modificar(request,id):
    try:
        mas = Mascota.objects.get(nombre=id)
        categorias= Categoria.objects.all()
        context = {"categorias":categorias,"mascota":mas}
        return render(request, "modificar.html",context)
    except:
        mensaje="no encontro mascota"

    mascotas = Mascota.objects.all()  
    categorias= Categoria.objects.all()
    context = {"categorias":categorias,"mensaje":mensaje,"mascotas":mascotas}
    return render(request, "registro.html",context)    

@login_required(login_url='/login/')
@permission_required('misPerris.change_mascota',login_url='/login/')
def modificar(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        edad = request.POST.get("txtEdad")
        desc = request.POST.get("txtDesc")
        cate = request.POST.get("cboCategoria")
        obj_cate = Categoria.objects.get(nombre=cate) # select * from Categoria where nombre=''
        imagen = request.FILES.get("txtImg")
        
        try:
            mas = Mascota.objects.get(nombre=nombre)
            mas.edad = edad
            mas.descripcion = desc
            mas.categoria = obj_cate

            if imagen is not None:
                mas.imagen = imagen
            
            mas.comentario = '--'
            mas.save()
            mensaje="modifico mascota"
        except:
            mensaje="no modifico"

    categorias = Categoria.objects.all() # select * from Categoria
    mascotas = Mascota.objects.filter(usuario = request.user.username)  
    context = {"categorias":categorias,"mensaje":mensaje,"mascotas":mascotas}
    return render(request, "registro.html",context)    

def adoptar(request,id):
    mensaje=""
    try:
        mas = Mascota.objects.filter(publicar=True).get(nombre=id)
        mas.dueno = request.user.username
        mas.publicar = False
        mas.save()
        mensaje="Adoptada"
    except:
        mensaje="No Pudo Adoptar la Mascota"
    
    mascota= Mascota.objects.get(nombre=id)
    contexto = {"mascota":mascota,"mensaje":mensaje}
    return render(request, "ficha.html",contexto)

def admin_usuario(request):
    mascotas = Mascota.objects.filter(dueno=request.user.username)
    contexto = {"mascotas":mascotas}
    return render(request,"admin_usuario.html",contexto)

def devolver(request,id):
    try:
        mas = Mascota.objects.filter(publicar=False).get(nombre=id)
        mas.dueno='--'
        mas.save()
        mensaje = "Mascota Devuelta"
    except:
        mensaje= "No Pudo devolver la mascota"
    
    mascotas = Mascota.objects.filter(dueno=request.user.username)
    contexto = {"mascotas":mascotas,"mensaje":mensaje}
    return render(request,"admin_usuario.html",contexto)

def insertar_galeria(request):
    mensaje=""
    if request.POST:
        nom_mascota = request.POST.get("txtMascota")
        imagen = request.FILES.get("txtImg")
        obj_masc = Mascota.objects.get(nombre=nom_mascota)

        gale = Galeria()
        gale.imagen = imagen
        gale.mascota = obj_masc
        gale.save()
        mensaje="Grabo Imagen Galeria para Mascota "+nom_mascota

    usuario = request.user.username
    mascotas = Mascota.objects.filter(usuario=usuario) 
    categorias = Categoria.objects.all() 
    context = {"categorias":categorias,"mensaje":mensaje,"mascotas":mascotas}
    return render(request, "registro.html",context)



########################################################
## clases
########################################################

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()