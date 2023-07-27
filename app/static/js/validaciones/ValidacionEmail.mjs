import { ValidacionBase } from "./ValidacionBase.mjs";

export class ValidacionEmail extends ValidacionBase {
  /**
   * Valida el email usando el standart RFC2822 - regexr.com/2rhq7
   * Esto no es suficiente, hay que validar enviando un email
   * No valida emails que comiencen con @@ como "@@double.at.sign@domain.com"
   * o emails con caracteres especiales como "special_characters!#&@domain.com"
   * @param {string} email El email a validar
   * @returns true o false dependiendo si el email es valido
   */
  validarEmail(email) {
    const regex = new RegExp(
      "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    );
    return regex.test(email);
  }

  /**
   * Valida si un elemento es un email
   * @param {HTMLElement} element El elemento HTML a validar
   */
  validar(element) {
    this.throwErrorIfNullElement(element);
    let valor = this.extraerValor(element);
    if (valor === "") {
      // Se retorna true, porque validar si un campo esta lleno o no, es tarea de Requerido
      return {
        error: false,
        message:
          "El email estaba vacio, pero no hubo error ya que validar si un elemento tiene valor o no es tarea de Requerido",
      };
    }
    if (!this.validarEmail(valor)) {
      return { error: true, message: "El elemento no es un email válido" };
    } else return { error: false };
  }
}
