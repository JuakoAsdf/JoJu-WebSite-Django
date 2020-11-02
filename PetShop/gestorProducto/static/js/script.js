//Sucesos a esperar
document.getElementById("btn_iniciar-sesion").addEventListener("click", iniciarSesion);
document.getElementById("btn_registrarse").addEventListener("click", register);
window.addEventListener("resize", anchoPagina);
//Declaración de variables
var contenedor__login_register = document.querySelector(".contenedor_login-register");
var formulario__login = document.querySelector(".formulario_login");
var formulario__register = document.querySelector(".formulario_register");
var caja_trasera_login = document.querySelector(".caja_trasera-login");
var caja_trasera_register = document.querySelector(".caja_trasera-register");
//Valores de ajuste
function anchoPagina(){
	if(window.innerWidth > 850){
		caja_trasera_login.style.display = "block";
		caja_trasera_register.style.display = "block";
	}else{
		caja_trasera_register.style.display = "block";
		caja_trasera_register.style.opacity = "1";
		caja_trasera_login.style.display = "none";
		formulario__login.style.display = "block";
		formulario__register.style.display = "none";
		contenedor__login_register.style.left = "0px";	
	}
}
anchoPagina();
function iniciarSesion(){
	if(window.innerWidth > 850){
	formulario__register.style.display = "none";
	contenedor__login_register.style.left = "10px";
	formulario__login.style.display = "block";
	caja_trasera_register.style.opacity = "1";
	caja_trasera_login.style.opacity= "0";	
	}else{
	formulario__register.style.display = "none";
	contenedor__login_register.style.left = "0px";
	formulario__login.style.display = "block";
	caja_trasera_register.style.display = "block";
	caja_trasera_login.style.display= "none";	
	}
}
function register(){	
	if(window.innerWidth > 850){			
	formulario__register.style.display = "block";
	contenedor__login_register.style.left = "410px";
	formulario__login.style.display = "none";
	caja_trasera_register.style.opacity = "0";
	caja_trasera_login.style.opacity= "1";	
	}else{
	formulario__register.style.display = "block";
	contenedor__login_register.style.left = "0px";
	formulario__login.style.display = "none";
	caja_trasera_register.style.display = "none";
	caja_trasera_login.style.display = "block";
	caja_trasera_login.style.opacity = "1";
	}
}






