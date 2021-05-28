function mensaje() {
    var nombre = document.getElementById('txtNombre').value;
    alert('Yo Soy :' + nombre);
}

function validarForm() {
    var resp = validarut();
    if (resp==false) {
        return false;
    }
    resp = validaFecha();
    if (resp==false) {
        return false;
    }
    resp = validaNombre();
    if (resp== false) {
        return false;
    }
    return true;
}

////////////////////////////// funciones de validacion
function validaFecha() {
    var fechaUsuario= document.getElementById('txtFechaNaci').value;
    console.log('Fecha Usuario:'+fechaUsuario);
    var fechaSistema = new Date();
    console.log('Fecha Sistema:'+fechaSistema);
    ///////////////////////////////////////////////
    var ano = fechaUsuario.slice(0,4);
    var mes = fechaUsuario.slice(5,7);
    var dia = fechaUsuario.slice(8,10);
    console.log('Año:'+ano+' Mes:'+mes+' Dia:'+dia);
    ///////////////////////////////////////////////
    var fechaNuevaUsuario = new Date(ano,(mes-1),dia);
    console.log('Nueva Fecha Usuario:'+fechaNuevaUsuario);
    if (fechaNuevaUsuario >= fechaSistema) {
        //alert('Fecha incorrecta');
        Swal.fire({
            icon: 'error',
            title: 'fecha de nacimiento',
            text: 'la fecha de nacimiento es mayor a la fecha actual'
          });
        return false;
    }
    ///////////////////////////////////////////////////
    var unDia = 24 * 60 * 60 * 1000;//cuantos milisegundos es un dia
    var diferencia_dias =Math.trunc( ( fechaSistema.getTime() - fechaNuevaUsuario.getTime() ) / unDia);
    console.log('Dias:'+diferencia_dias);
    var anos =Math.trunc( diferencia_dias / 365 );
    console.log('Años:'+anos);
    if (anos<18) {
        //alert('es menor de edad, usted tiene '+anos+ ' años de edad');
        Swal.fire({
            icon: 'error',
            title: 'fecha de nacimiento',
            text: 'es menor de edad, usted tiene '+anos+ ' años de edad'
          });
        return false;
    }
    return true;
}
function validarut() {
    var rut = document.getElementById('txtRut').value;
    if ( rut.length !=10 ) {
        //alert('largo del rut incorrecto');
        Swal.fire({
            icon: 'error',
            title: 'rut',
            text: 'el largo del rut es incorrecto'
          });
        return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var carac= rut.slice(index,index+1);
        //alert(carac + ' x '+ num);
        console.log(carac + ' x '+ num);
        suma = suma + ( carac * num );
        num=num-1;
        if (num == 1) {
            num = 7;
        }
    }
    // alert(' Total: '+suma);
    console.log(' Total: '+suma);
    var resto = suma % 11;
    var dv = 11 - resto;
    
    if ( dv > 9) {
        if ( dv == 10 ) {
            dv ='K';
        }else{
            dv=0;
        }
    }
    console.log('DV:'+dv);
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        //alert('Rut incorrecto');
        //Swal.fire('el rut es incorrecto, verifiquelo');
        Swal.fire({
            icon: 'error',
            title: 'rut',
            text: 'el digito verificador del rut es incorrecto'
          });
        return false;
    }
    return true;
}
function validaNombre() {
    var nombre = document.getElementById('txtNombre').value;
    if (nombre.trim().length < 3) {
        //alert('el nombre debe tener un minimo de 3 caracter');
        Swal.fire({
            icon: 'error',
            title: 'nombre',
            text: 'el nombre debe tener un minimo de 3 caracteres'
          });
        return false;
    }
    return true;
}