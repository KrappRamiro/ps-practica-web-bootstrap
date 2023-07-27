"""
The filters.py file is responsible for defining custom Jinja filters used in the Flask project.
Jinja filters allow modifying or formatting data within templates.
"""
from app import app


def reemplazar_vocales_con_tildes(texto):
    # Diccionario de reemplazos
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U",
    }

    # Realizamos los reemplazos
    for tildada, normal in reemplazos.items():
        texto = texto.replace(tildada, normal)

    return texto


@app.template_filter("clean_text")
def clean_text(text):
    """
    Custom Jinja filter to replace whitespaces and special characters with dashes in a text.
    Usage:

    To use this custom filter in a template, you can apply it using
    the | operator and the filter name, clean_text.
    For example:
    {{ my_text|clean_text }}

    Args:
        text (str): The input text.

    Returns:
        str: The text with whitespaces and special characters replaced by dashes.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    text = (
        reemplazar_vocales_con_tildes(text)
        .replace(" ", "-")
        .replace("(", "")
        .replace(")", "")
        .replace("¿", "")
        .replace("?", "")
    )

    return text
