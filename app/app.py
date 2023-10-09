from flask import Flask

from .presentation import views
from .business import services
from .data import models


app = Flask(__name__)


app.config["SECRET_KEY"] = "my-secret-key"

if __name__ == "__main__":
    app.run(debug=True)
