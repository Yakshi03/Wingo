from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Wingo Predictor Running Successfully!"

@app.route("/predict")
def predict():
    return jsonify({"prediction": "Small", "confidence": 0.82})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
