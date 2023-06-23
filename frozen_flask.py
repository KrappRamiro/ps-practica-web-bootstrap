from app import app
from flask_frozen import Freezer  # Added

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
