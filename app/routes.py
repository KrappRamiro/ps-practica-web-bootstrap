from app import app
from flask import render_template, request, session, jsonify, redirect


@app.route("/")
def index():
    steps = [
        {
            "number": 1,
            "title": "Elegí tu seguro",
            "status": "current",
        },
        {
            "number": 2,
            "title": "Carga los datos de tu auto",
            "status": "current",
        },
        {
            "number": 3,
            "title": "Elegí tu plan a medida",
            "status": "current",
        },
        {
            "number": 4,
            "title": "Carga tus datos personales",
            "status": "current",
        },
        {
            "number": 5,
            "title": "Confirma tus datos",
            "status": "current",
        },
    ]

    return render_template("index.html", title="Home", steps=steps)


@app.route("/picker/")
def picker():
    steps = [
        {
            "number": 1,
            "title": "Elegí tu seguro",
            "status": "current",
        },
        {
            "number": 2,
            "title": "Carga los datos de tu auto",
            "status": "pending",
        },
        {
            "number": 3,
            "title": "Elegí tu plan a medida",
            "status": "pending",
        },
        {
            "number": 4,
            "title": "Carga tus datos personales",
            "status": "pending",
        },
        {
            "number": 5,
            "title": "Confirma tus datos",
            "status": "pending",
        },
    ]

    return render_template("picker.html", title="Picker", steps=steps)


@app.route("/ingreso-datos-automotor/")
def ingreso_datos_automotor():
    steps = [
        {
            "number": 1,
            "title": "Elegí tu seguro",
            "status": "pending",
        },
        {
            "number": 2,
            "title": "Carga los datos de tu auto",
            "status": "current",
        },
        {
            "number": 3,
            "title": "Elegí tu plan a medida",
            "status": "pending",
        },
        {
            "number": 4,
            "title": "Carga tus datos personales",
            "status": "pending",
        },
        {
            "number": 5,
            "title": "Confirma tus datos",
            "status": "pending",
        },
    ]
    forms = [
        {
            "title": "Datos del vehículo",
            "inputs": [
                {
                    "type": "select",
                    "label": "Marca",
                    "placeholder": "Placeholder",
                    "options": ["Peugeot", "Chevrolet", "Audi"],
                    "helptext": "Help!",
                },
                {
                    "type": "radio",
                    "label": "¿Es Cero KM?",
                    "placeholder": "Placeholder",
                    "options": ["Si", "No"],
                },
                {
                    "type": "select",
                    "select-multiple": True,
                    "label": "Accesorios",
                    "placeholder": "Placeholder",
                    "options": ["AC", "Airbag pro +"],
                },
                {
                    "type": "select",
                    "label": "Año de fabricación",
                    "placeholder": "Placeholder",
                    "options": ["2012", "2013", "2014", "2015"],
                },
                {
                    "type": "select",
                    "label": "Modelo",
                    "placeholder": "Placeholder",
                    "size": "double",
                    "options": ["Berlingo", "Kangoo", "Corsa", "Daytona", "Gol"],
                },
            ],
        }
    ]

    return render_template(
        "ingreso-datos-automotor.html", title="Picker", steps=steps, forms=forms
    )
