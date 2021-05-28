from django.contrib import admin
from django.urls import path
from .views import insertar_galeria, devolver, admin_usuario, adoptar, modificar, buscar_modificar, eliminar, cerrar_sesion, login, index, galeria,filtro_categoria,filtro_cate,filtro_descripcion, formulario,ficha ,contacto, quienes,formvalida, registro

urlpatterns = [
    path('',index,name='IND'),
    path('gale/',galeria,name='GALE'),
    path('formu/',formulario,name='FORMU'),
    path('contacto/',contacto,name='CONT'),
    path('quienes/',quienes,name='QUIEN'),
    path('form2/',formvalida, name='FORM2'),
    path('registro/',registro,name='REG'),
    path('ficha/<id>/',ficha,name='FICHA'),
    path('filtro_c/',filtro_categoria,name='FILTROC'),
    path('filtro_d/',filtro_descripcion,name='FILTROD'),
    path('filtro_cate/<id>/',filtro_cate,name='FILTROCATE'),
    path('login/',login,name='LOGIN'),
    path('cerrar/',cerrar_sesion,name='CERRAR'),
    path('eliminar/<id>/',eliminar,name="ELIMINAR"),
    path('buscar_modificar/<id>/',buscar_modificar,name='BUSCARM'),
    path('modificar/',modificar,name='MODI'),
    path('adoptar/<id>/',adoptar,name='ADOPTAR'),
    path('admin_usuario/',admin_usuario,name='ADMINUSUARIO'),
    path('devolver/<id>/',devolver,name='DEVOLVER'),
    path('insertar_galeria/',insertar_galeria,name='INSERTARG'),
]
# {% url ' ' %}