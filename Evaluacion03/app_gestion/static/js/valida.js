// const $formulario=document.getElementById('formulario')
// const $txtnombre=document.getElementById('txtnombre');
// (function(){
//     $formulario.addEventListener('submit', function (e){
//        let nombre = String($txtnombre.value).trim();
//        if (nombre == 0){
//         alert("el campo nombre no puede ir vacío...")
//        }
//         e.preventDefault();
//     })
// })();

// const $txtApPaterno=document.getElementById('txtApPaterno');
// (function(){
//     $formulario.addEventListener('submit', function (e){
//        let ap_paterno = String($txtApPaterno.value).trim();
//        if (ap_paterno == 0){
//         alert("el campo apellido paterno no puede ir vacío...")
//        }
//         e.preventDefault();
//     })
// })();
// const $txtApMaterno=document.getElementById('txtApMaterno');
// (function(){
//     $formulario.addEventListener('submit', function (e){
//        let ap_materno = String($txtApMaterno.value).trim();
//        if (ap_materno == 0){
//         alert("el campo apellido materno no puede ir vacío...")
//        }
//         e.preventDefault();
//     })
// })();
// const $txtVacuna=document.getElementById('txtVacuna');
// (function(){
//     $formulario.addEventListener('submit', function (e){
//        let vacuna = String($txtVacuna.value).trim();
//        if (vacuna == 0){
//         alert("el campo vacuna no puede ir vacío...")
//        }
//         e.preventDefault();
//     })
// })();

function validar(){
    rut=document.formulario.txtRut.value;
    nombre=document.formulario.txt_nombre.value;
    ap_paterno=document.formulario.txtApPaterno.value;
    ap_materno=document.formulario.txtApMaterno.value;
    vacuna  =document.formulario.txtVacuna.value;
    edad  =document.formulario.numberEdad.value;


    
    if (rut<=7) {
        alert("El campo rut no puede ir vacio...");
            document.formulario.txtRut.focus();
        return false;
        }
     if (edad<=7) {
         alert("El campo edad no puede ir vacio...");
            document.formulario.numberEdad.focus();
        return false;
       }

    if (nombre.length<=2)
    {
        alert("el campo nombre no puede ir vacio...");
        document.formulario.txt_nombre.focus();
        return false;
    }
    if (ap_paterno.length<=2){
        alert("El campo apellido parterno no puede ir vacio...");
        document.formulario.txtApPaterno.focus();
        return false;
    }
    if (ap_materno.length<=2){
        alert("El campo apellido marterno no puede ir vacio...");
        document.formulario.txtApMaterno.focus();
        return false;
    }
    if (vacuna.length<=2){
        alert("El campo vacuna no puede ir vacio...");
        document.formulario.txtVacuna.focus();
        return false;
    }



    document.formulario.action="/ingreso_persona/"
    document.formulario.submit()=true
    alert("ingreso exitoso...");
}

function validardom(){
    nombre_completo=document.formulario2.txtnombreCom.value;
    direccion=document.formulario2.txtDireccion.value;
    comuna=document.formulario2.txtComuna.value;
    telefono=document.formulario2.txtTelefono.value;
    rut=document.formulario2.txtRut.value;




    if (nombre_completo.length<=6){
        alert("El campo nombre completo no puede ir vacio...");
        document.formulario2.txtnombreCom.focus();
        return false;
    }
    if (direccion.length<=5){
        alert("El campo dierccion no puede ir vacio...");
        document.formulario2.txtDireccion.focus();
        return false;
    }
    if (comuna.length<=5){
        alert("El campo comuna no puede ir vacio...");
        document.formulario2.txtComuna.focus();
        return false;
    }
    if (telefono<=9) {
        alert("El campo telefono no puede ir vacio...");
            document.formulario2.txtTelefono.focus();
        return false;
        }
        if (rut<=7) {
            alert("El campo rut no puede ir vacio...");
                document.formulario2.txtRut.focus();
            return false;
            }
        
    
    
document.formulario2.action="/ingreso_dom/"
document.formulario2.submit()=true
alert("ingreso exitoso...");
}