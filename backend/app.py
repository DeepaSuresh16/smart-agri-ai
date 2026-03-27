from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Smart Agriculture AI is Running 🚀"

@app.route('/predict_crop', methods=['POST'])
def predict_crop():
    data = request.json
    
    # TEMP (dummy logic)
    if data['N'] > 50:
        crop = "Rice 🌾"
    else:
        crop = "Wheat 🌿"

    return jsonify({'recommended_crop': crop})

if __name__ == '__main__':
    app.run(debug=True)
