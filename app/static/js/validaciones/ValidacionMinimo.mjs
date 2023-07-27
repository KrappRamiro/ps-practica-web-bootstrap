import { ValidacionBase } from "./ValidacionBase.mjs";

export class ValidacionMinimo extends ValidacionBase {
  constructor(minimo) {
    super();
    if (typeof minimo !== "number" || isNaN(minimo)) {
      throw new TypeError(
        `El Validacion Minimo espera que minimo sea un número, pero recibió un ${typeof minimo}`
      );
    }
    if (minimo < 0) {
      throw new RangeError("minimo debe tener un valor mayor a 0");
    }
    this.minimo = minimo;
  }

  validar(element) {
    this.throwErrorIfNullElement(element);
    let valor = this.extraerValor(element).toString();
    if (valor.length < this.minimo) {
      return {
        error: true,
        message: `El elemento tiene que ser mayor a ${this.minimo} caracteres`,
      };
    } else return { error: false };
  }
}
