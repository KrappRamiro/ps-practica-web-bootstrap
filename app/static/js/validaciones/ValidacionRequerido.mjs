import { ValidacionBase } from "./ValidacionBase.mjs";

export class ValidacionRequerido extends ValidacionBase {
	/**
	 * Valida si un elemento tiene valor o no
	 * @param {HTMLElement} element El elemento HTML a validar
	 */
	validar(element) {
		this.throwErrorIfNullElement(element);
		let valor = this.extraerValor(element);
		let name = element.name || "elemento";
		if (!valor) {
			name = name.replace(/-/g, " ");
			return { error: true, message: `El elemento ${name} es requerido` };
		} else return { error: false };
	}
}
