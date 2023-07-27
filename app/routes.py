from app import app
from flask import render_template, request, session, jsonify, redirect
import random

STEPS = [
    "Elegí tu seguro",
    "Carga los datos de tu auto",
    "Elegí tu plan a medida",
    "Carga tus datos personales",
    "Confirma tus datos",
]
LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse at dolor nibh. Nunc felis lacus, ullamcorper nec feugiat id, viverra at velit. Vestibulum fermentum lectus sit amet varius eleifend. Nullam rhoncus sodales nulla, non bibendum mi consectetur vel. Nunc nisi libero, aliquam et rutrum ut, interdum non magna. Vestibulum laoreet enim urna, a elementum lacus ultrices et. Vestibulum bibendum, felis quis cursus semper, arcu urna condimentum lorem, eget ultrices sem felis quis ligula. Integer luctus nunc quis dictum auctor. In gravida tristique nulla eget imperdiet."


@app.route("/")
def index():
    beneficios = [
        {
            "icon": "fa-piggy-bank",
            "title": "Ahorra",
            "type": "text",
            "description": "Con Provincia Seguros, ahorrá mucha mucha plata",
        },
        {
            "icon": "fa-mobile",
            "title": "Comunicate",
            "type": "text",
            "description": "Podes usar tu celular para comunicarte",
        },
        {
            "icon": "fa-comments",
            "title": "Contactate",
            "type": "text",
            "description": "Atencion 100\% personalizada",
        },
        {
            "icon": "fa-truck-arrow-right",
            "title": "En el instante",
            "type": "text",
            "description": "Todo se hace al instante",
        },
        {
            "icon": "fa-piggy-bank",
            "title": "Ahorra",
            "type": "text",
            "description": "Con Provincia Seguros, ahorrá mucha mucha plata",
        },
        {
            "icon": "fa-piggy-bank",
            "title": "Ahorra",
            "type": "text",
            "description": "Con Provincia Seguros, ahorrá mucha mucha plata",
        },
    ]
    faq = [
        {
            "title": "¿Cómo puedo pagar mi seguro?",
            "description": "Respuesta",
        },
        {
            "title": "¿Cuándo puedo darme de baja?",
            "description": "Respuesta",
        },
        {
            "title": "¿A partir de qué momento tengo cobertura? ¿Cuánto dura?",
            "description": "Respuesta",
        },
        {
            "title": "¿Qué es la franquicia?",
            "description": "Respuesta",
        },
        {
            "title": "¿Provincia Seguros tiene que inspeccionar mi auto para asegurarlo?",
            "description": "Respuesta",
        },
        {
            "title": "¿Qué pasa si pierdo mi documentación?",
            "description": "Respuesta",
        },
    ]
    return render_template(
        "index.html",
        title="Home",
        steps=STEPS,
        current_step="all",
        horizontal_cards=beneficios,
        faq=faq,
    )


@app.route("/picker/")
def picker():
    return render_template("picker.html", title="Picker", steps=STEPS, current_step=1)


@app.route("/ingreso-datos-automotor/")
def ingreso_datos_automotor():
    forms = [
        {
            "title": "Datos del vehículo",
            "inputs": [
                {
                    "type": "select",
                    "label": "Marca",
                    "options": ["Peugeot", "Chevrolet", "Audi"],
                    "helptext": "Help!",
                },
                {
                    "type": "radio",
                    "label": "¿Es Cero KM?",
                    "options": ["Si", "No"],
                },
                {
                    "type": "select",
                    "select-multiple": True,
                    "label": "Accesorios",
                    "options": ["AC", "Airbag pro +"],
                },
                {
                    "type": "select",
                    "label": "Año de fabricación",
                    "options": ["2012", "2013", "2014", "2015"],
                },
                {
                    "type": "select",
                    "label": "Modelo",
                    "size": "double",
                    "options": ["Berlingo", "Kangoo", "Corsa", "Daytona", "Gol"],
                },
            ],
        }
    ]

    return render_template(
        "ingreso-datos-automotor.html",
        title="Ingreso de datos automotor",
        steps=STEPS,
        current_step=2,
        forms=forms,
    )


@app.route("/cotizacion/")
def cotizacion():
    horizontal_cards = [
        {
            "icon": "fa-solid fa-car",
            "title": "Datos del vehículo",
            "type": "list",
            "items": [
                "FIORINO FURGON COMFORT AÑO 2010",
                "Cotización Nro 86471769",
                "Suma asegurada: $2.057.000",
                "Equipo de rastreo obligatorio 21752 - No",
                "Uso: 21729 - Particular",
            ],
        },
        {
            "icon": "fa-solid fa-shield",
            "title": "Datos del vehículo",
            "type": "list",
            "items": [
                "FIORINO FURGON COMFORT AÑO 2010",
                "Cotización Nro 86471769",
                "Suma asegurada: $2.057.000",
                "Equipo de rastreo obligatorio 21752 - No",
                "Uso: 21729 - Particular",
            ],
        },
    ]
    pricing_cards = [
        {
            "title": "Basico",
            "old_price": 20635,
            "promo_price": 16762,
            "infolines": [
                "Daño Total por Accidente",
                "Cubierta/ llanta hasta 1",
                "Cubierta/ llanta hasta 1",
                "Daño Parcial por Robo Total",
                "Robo/lnc Parcial S/Fcia.",
                "Cubierta/ llanta hasta 1",
                "Daño Parcial por Robo Total",
                "Robo/lnc Parcial S/Fcia.",
                "Auto Sustituto 5 días",
            ],
            "extra_info": LOREM_IPSUM,
        },
        {
            "title": "Todo riesgo",
            "featured": True,
            "old_price": 30793,
            "promo_price": 24793,
            "infolines": [
                "Daño Total por Accidente",
                "Robo/lnc Parcial S/Fcia.",
                "Auto Sustituto 5 días",
                "Cubierta/ llanta hasta 1",
                "Daño Parcial por Robo Total",
                "Robo/lnc Parcial S/Fcia.",
                "Auto Sustituto 5 días",
                "Cubierta/ llanta hasta 1",
                "Daño Parcial por Robo Total",
                "Robo/lnc Parcial S/Fcia.",
                "Auto Sustituto 5 días",
            ],
            "extra_info": LOREM_IPSUM,
        },
        {
            "title": "Premium",
            "old_price": 26701,
            "promo_price": 22877,
            "infolines": [
                "Daño Parcial por Robo Total",
                "Daño Parcial por Robo Total",
                "Robo/lnc Parcial S/Fcia",
                "Cubierta/ llanta hasta 1",
                "Robo/lnc Parcial S/Fcia",
                "Cubierta/ llanta hasta 1",
            ],
            "extra_info": LOREM_IPSUM,
        },
    ]
    return render_template(
        "cotizacion.html",
        title="Cotización",
        steps=STEPS,
        current_step=3,
        horizontal_cards=horizontal_cards,
        pricing_cards=pricing_cards,
    )


@app.route("/ingreso-datos-personales/")
def ingreso_datos_personales():
    forms = [
        {
            "title": "Datos Personales",
            "inputs": [
                {
                    "type": "text",
                    "label": "Nombre",
                },
                {
                    "type": "text",
                    "label": "Apellido",
                },
                {
                    "type": "text",
                    "label": "Numero de documento (DNI)",
                },
                {
                    "type": "date",
                    "label": "Fecha de Nacimiento",
                },
                {
                    "type": "select",
                    "label": "Género",
                    "options": [
                        "Femenino",
                        "Masculino",
                        "No binario",
                        "Agénero",
                        "Bigénero",
                        "Género fluido",
                        "Género no conforme",
                        "Cuestionamiento de género",
                        "Género no conformista",
                        "Transgénero",
                        "Hombre transgénero",
                        "Mujer transgénero",
                        "Pangénero",
                        "Neutrois",
                        "Demigénero",
                        "Demimujer",
                        "Demihombre",
                        "Tercer género",
                        "Otro",
                    ],
                    "helptext": "Nota: Hay muchas opciones :S",
                },
                {
                    "type": "select",
                    "label": "Estado Civil",
                    "options": ["Soltero", "Casado", "Viudo", "Divorciado"],
                },
                {
                    "type": "select",
                    "label": "Nacionalidad",
                    "options": [
                        "Afgana",
                        "Alemana",
                        "Americana",
                        "Argentina",
                        "Australiana",
                        "Austriaca",
                        "Belga",
                        "Boliviana",
                        "Brasileña",
                        "Canadiense",
                        "Chilena",
                        "China",
                        "Colombiana",
                        "Coreana",
                        "Costarricense",
                        "Cubana",
                        "Danesa",
                        "Dominicana",
                        "Ecuatoriana",
                        "Egipcia",
                        "Española",
                        "Estadounidense",
                        "Filipina",
                        "Finlandesa",
                        "Francesa",
                        "Griega",
                        "Guatemalteca",
                        "Hindú",
                        "Holandesa",
                        "Hondureña",
                        "Indonesia",
                        "Inglesa",
                        "Irlandesa",
                        "Italiana",
                        "Jamaicana",
                        "Japonesa",
                        "Mexicana",
                        "Noruega",
                        "Panameña",
                        "Paraguaya",
                        "Peruana",
                        "Polaca",
                        "Portuguesa",
                        "Puertorriqueña",
                        "Rusa",
                        "Sueca",
                        "Suiza",
                        "Uruguaya",
                        "Venezolana",
                    ],
                },
                {
                    "type": "text",
                    "label": "Profesion",
                },
            ],
        },
        {
            "title": "Datos de Contacto",
            "inputs": [
                {
                    "type": "tel",
                    "label": "Telefono",
                    "helptext": "Ingresa tu número incluyendo el código de área",
                },
                {
                    "type": "tel",
                    "label": "Celular",
                    "helptext": "Ingresa tu número incluyendo el código de área",
                },
                {
                    "type": "email",
                    "label": "Correo electrónico (email)",
                },
            ],
        },
        {
            "title": "Domicilio",
            "inputs": [
                {
                    "type": "select",
                    "label": "Provincia",
                    "options": ["Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "Entre Ríos"],
                },
                {
                    "type": "select",
                    "label": "Localidad",
                    "options": [
                        "Temperley",
                        "Lomas de Zamora",
                        "Lanus",
                        "Quilmes",
                        "Villa Adelina",
                        "Pilar",
                    ],
                },
                {
                    "type": "text",
                    "label": "Código Postal",
                },
                {
                    "type": "text",
                    "label": "Calle",
                },
                {
                    "type": "number",
                    "label": "Numero",
                },
                {
                    "type": "text",
                    "label": "Piso",
                },
                {
                    "type": "text",
                    "label": "Departamento",
                },
                {
                    "type": "text",
                    "label": "Unidad",
                },
            ],
        },
        {
            "title": "Datos del vehículo",
            "inputs": [
                {
                    "type": "text",
                    "label": "Patente",
                },
                {
                    "type": "text",
                    "label": "Número de Motor",
                },
                {
                    "type": "text",
                    "label": "Número de chasis",
                },
            ],
        },
        {
            "title": "Datos de Inspección",
            "inputs": [
                {
                    "type": "num",
                    "label": "Telefono Celular",
                    "helptext": "Ingresa tu número incluyendo el código de área",
                },
                {
                    "type": "text",
                    "label": "Número de chasis (inspec)",
                },
            ],
        },
        {
            "title": "Forma de Pago",
            "inputs": [
                {
                    "type": "select",
                    "label": "¿Cómo querés pagar?",
                    "options": [
                        "Efectivo",
                        "Transferencia Bancaria",
                        "Débito automático",
                        "Riñon",
                    ],
                },
            ],
        },
    ]

    return render_template(
        "ingreso-datos-personales.html",
        title="Ingreso de datos personales",
        steps=STEPS,
        current_step=4,
        forms=forms,
    )


@app.route("/confirmacion/")
def confirmacion():
    return render_template(
        "confirmacion.html",
        title="Confirmacion",
        steps=STEPS,
        current_step=5,
        image=random.randint(1, 4),
    )


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404
