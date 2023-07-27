import { Validatron } from "../Validatron.mjs";
import { ValidacionEmail } from "../validaciones/ValidacionEmail.mjs";
import { ValidacionRequerido } from "../validaciones/ValidacionRequerido.mjs";

const validatron = new Validatron();

const form = document.querySelector("#form-ingreso-datos-personales");
const nombre = document.querySelector("#Nombre");
const apellido = document.querySelector("#Apellido");
const numeroDNI = document.querySelector("#Numero-de-documento-DNI");
const fechaNacimiento = document.querySelector("#Fecha-de-Nacimiento");
const genero = document.querySelector("#Genero");
const estadoCivil = document.querySelector("#Estado-Civil");
const profesion = document.querySelector("#Profesion");
const telefono = document.querySelector("#Telefono");
const celular = document.querySelector("#Celular");
const email = document.querySelector("#Correo-electronico-email");
const provincia = document.querySelector("#Provincia");
const localidad = document.querySelector("#Localidad");
const codigoPostal = document.querySelector("#Codigo-Postal");
const calle = document.querySelector("#Calle");
const numeroCalle = document.querySelector("#Numero");
const piso = document.querySelector("#Piso");
const departamento = document.querySelector("#Departamento");
const unidad = document.querySelector("#Unidad");
const patente = document.querySelector("#Patente");
const numeroMotor = document.querySelector("#Numero-de-Motor");
const numeroChasis = document.querySelector("#Numero-de-chasis");
const telefonoCelularInspeccion = document.querySelector("#Telefono-Celular");
const numeroChasisInspeccion = document.querySelector("#Numero-de-chasis-inspec");
const formaPago = document.querySelector("#Como-queres-pagar");

validatron.registrarElemento(nombre, [ValidacionRequerido]);
validatron.registrarElemento(apellido, [ValidacionRequerido]);
validatron.registrarElemento(numeroDNI, [ValidacionRequerido]);
validatron.registrarElemento(fechaNacimiento, [ValidacionRequerido]);
validatron.registrarElemento(genero, [ValidacionRequerido]);
validatron.registrarElemento(estadoCivil, [ValidacionRequerido]);
validatron.registrarElemento(profesion, [ValidacionRequerido]);
validatron.registrarElemento(telefono, [ValidacionRequerido]);
validatron.registrarElemento(celular, [ValidacionRequerido]);
validatron.registrarElemento(email, [ValidacionRequerido, ValidacionEmail]);
validatron.registrarElemento(provincia, [ValidacionRequerido]);
validatron.registrarElemento(localidad, [ValidacionRequerido]);
validatron.registrarElemento(codigoPostal, [ValidacionRequerido]);
validatron.registrarElemento(calle, [ValidacionRequerido]);
validatron.registrarElemento(numeroCalle, [ValidacionRequerido]);
validatron.registrarElemento(patente, [ValidacionRequerido]);
validatron.registrarElemento(numeroMotor, [ValidacionRequerido]);
validatron.registrarElemento(numeroChasis, [ValidacionRequerido]);
validatron.registrarElemento(telefonoCelularInspeccion, [ValidacionRequerido]);
validatron.registrarElemento(numeroChasisInspeccion, [ValidacionRequerido]);
validatron.registrarElemento(formaPago, [ValidacionRequerido]);

document.addEventListener("DOMContentLoaded", function () {
	form.onsubmit = function (event) {
		event.preventDefault();
		validatron.ejecutarValidaciones();
		if (validatron.hayErorres()) {
			validatron.mostrarMensajesError();
			return false;
		}
		window.location.href = "../confirmacion"; //one level up
	};
});
