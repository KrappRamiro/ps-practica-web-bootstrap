import { ValidacionBase } from "./ValidacionBase.mjs";

export class ValidacionNumero extends ValidacionBase {
  /**
   * Valida si un elemento es un numero
   * @param {HTMLElement} element El elemento HTML a validar
   */
  validar(element) {
    this.throwErrorIfNullElement(element);
    let valor = parseFloat(this.extraerValor(element));
    //console.log(`Validando numerico tipo ${typeof valor} con valor ${valor}`)
    if (isNaN(valor)) {
      return { error: true, message: "El elemento no es un número" };
    } else return { error: false };
  }
}
