import { ValidacionBase } from "./ValidacionBase.mjs";

export class ValidacionRequerido extends ValidacionBase {
  /**
   * Valida si un elemento tiene valor o no
   * @param {HTMLElement} element El elemento HTML a validar
   */
  validar(element) {
    this.throwErrorIfNullElement(element);
    let valor = this.extraerValor(element);
    if (!valor) {
      return { error: true, message: "El elemento es requerido" };
    } else return { error: false };
  }
}
