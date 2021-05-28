class usuario{
    rut;
    nombre;
    apellido;
    fecha;
    // mutadores
    setRut(rut){
        this.rut=rut;
    }
    setNombre(nombre){ this.nombre=nombre;}
    setApellido(apellido){ this.apellido=apellido;}
    setFecha(fecha){ this.fecha= fecha;}
    // accesadores
    getRut(){
        return this.rut;
    }
    getNombre(){ return this.nombre;}
    getApellido(){ return this.apellido;}
    getFecha(){ return this.fecha;}

    imprimir(){
        return 'nombre:'+this.getNombre()+' Apellido:'+this.getApellido()
        +' rut:'+this.getRut();
    }

}