from app import app
from flask_frozen import Freezer

app.config["FREEZER_BASE_URL"] = "/ps-practica-web-bootstrap/"

freezer = Freezer(app)


if __name__ == "__main__":
    freezer.freeze()
