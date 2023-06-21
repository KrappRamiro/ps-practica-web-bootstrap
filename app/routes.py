from app import app
from flask import render_template, request, session, jsonify, redirect

@app.route('/')
def index():
    return render_template(
        "index.html",
        title="Home",
    )
