export class ValidacionBase {
  /**
   * Esta funcion extrae el valor de un elemento HTML cualquiera
   * @param {HTMLElement} element Element al cual le queremos extraer el valor
   */
  extraerValor(element) {
    return element.value;
  }
  throwErrorIfNullElement(element) {
    // tira un error si el elemento es null (o sea, no se encontró)
    if (element === null) {
      throw new Error("Elemento HTML no encontrado");
    }
  }
}
