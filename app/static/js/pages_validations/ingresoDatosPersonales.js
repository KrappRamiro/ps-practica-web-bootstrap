import { Validatron } from "../Validatron.mjs";
import { ValidacionEmail } from "../validaciones/ValidacionEmail.mjs";
import { ValidacionRequerido } from "../validaciones/ValidacionRequerido.mjs";

const validatron = new Validatron();

const form = document.querySelector("#form-ingreso-datos-personales");
const nombre = document.querySelector("#Nombre");
const apellido = document.querySelector("#Apellido");
const numeroDNI = document.querySelector("#Numero-de-documento-DNI");

validatron.registrarElemento(nombre, [ValidacionRequerido]);
validatron.registrarElemento(apellido, [ValidacionRequerido]);
validatron.registrarElemento(numeroDNI, [ValidacionRequerido]);

document.addEventListener("DOMContentLoaded", function () {
	form.onsubmit = function (event) {
		console.log("ejecutate porfis");
		event.preventDefault();
		validatron.ejecutarValidaciones();
		if (validatron.hayErorres()) {
			validatron.mostrarMensajesError();
			return false;
		}

		form.submit();
	};
});
