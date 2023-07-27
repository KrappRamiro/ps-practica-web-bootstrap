import { ValidacionBase } from "./validaciones/ValidacionBase.mjs";
import { ValidacionRequerido } from "./validaciones/ValidacionRequerido.mjs";
import { ValidacionEmail } from "./validaciones/ValidacionEmail.mjs";
import { ValidacionNumero } from "./validaciones/ValidacionNumero.mjs";

export class Validatron {
	registroElementos = [];
	constructor() {
		// console.log("Iniciando validatron");
	}

	/**
	 *
	 * @param {HTMLElement} elementoHTML El elemento HTML al que se le quiere registrar una validacion
	 * @param {Array.<ValidacionBase>} listaValidaciones Un array que contenga las validaciones asociadas al htmlElement
	 */
	registrarElemento(elementoHTML, listaValidaciones) {
		const nuevoElemento = {};
		nuevoElemento.elementoHTML = elementoHTML;
		nuevoElemento.validacionesAsociadas = listaValidaciones;
		nuevoElemento.resultado = {};
		console.log(
			`Se ha agregado el elemento ${nuevoElemento.elementoHTML} al registro de elementos`
		);
		this.registroElementos.push(nuevoElemento);
	}

	ejecutarValidaciones() {
		// console.log("Ejecutando validaciones!");
		// console.log(`Hay que validar ${this.registroElementos.length} elementos!`);
		this.registroElementos.forEach((elemento) => {
			// console.log(`Validando un ${elemento.elementoHTML} `);
			elemento.validacionesAsociadas.forEach((Validacion) => {
				// console.log(`Ejecutando la validación ${Validacion.name}`);
				const validacion = new Validacion();
				const resultado = validacion.validar(elemento.elementoHTML);
				elemento.resultado = resultado;
			});
		});
	}

	hayErorres() {
		// esto verifica si hay errores en el registroElementos
		let hayErorres = false;
		this.registroElementos.forEach((elemento) => {
			if (elemento.resultado.error === true) {
				hayErorres = true;
				return;
			}
		});
		return hayErorres;
	}

	getMensajesError() {
		let listaMensajesError = [];
		this.registroElementos.forEach((elemento) => {
			if (elemento.resultado.error === true) {
				listaMensajesError.push(elemento.resultado.message);
			}
		});
		return listaMensajesError;
	}

	getElementosError() {
		let listaElementosError = [];
		this.registroElementos.forEach((elemento) => {
			if (elemento.resultado.error === true) {
				listaElementosError.push(elemento);
			}
		});
		return listaElementosError;
	}

	alertarMensajesError() {
		const listaErrores = this.getMensajesError();
		listaErrores.forEach((mensajeError) => {
			alert(mensajeError);
		});
	}

	addErrorMessageToInputs() {
		const listaElementosError = this.getElementosError();
		listaElementosError.forEach((elemento) => {
			const elementoHTML = elemento.elementoHTML;
			if (!elementoHTML.classList.contains("is-validated")) {
				// Esto esta para evitar que se inserte el mensaje de error multiples veces si se clickea el boton de enviar
				// Si el elemento ya contiene "is-validated" como clase, no hace nada
				elementoHTML.classList.add("is-invalid", "is-validated");
				elementoHTML.insertAdjacentHTML(
					"afterend",
					"<div class='invalid-feedback'> Por favor revise... </div>"
				);
			}
		});
	}
}
