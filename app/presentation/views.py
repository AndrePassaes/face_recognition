from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]
    path = image.filename
    category = services.classify_image(path)
    return render_template("predicion.html", category=category)


if __name__ == "__main__":
    app.run(debug=True)
