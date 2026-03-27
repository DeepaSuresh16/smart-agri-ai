from flask import Flask, request, jsonify
from pyngrok import ngrok
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import threading

# 🔑 PASTE YOUR NGROK TOKEN HERE
ngrok.set_auth_token("PASTE_YOUR_TOKEN_HERE")

app = Flask(__name__)

# -------------------------------
# 🌾 TRAIN CROP MODEL
# -------------------------------
data = {
    'N':[90,40,60,30],
    'P':[40,50,30,20],
    'K':[40,20,60,10],
    'label':['rice','wheat','maize','cotton']
}

df = pd.DataFrame(data)

X = df[['N','P','K']]
y = df['label']

model = RandomForestClassifier()
model.fit(X,y)

# -------------------------------
# 🏠 HOME ROUTE
# -------------------------------
@app.route('/')
def home():
    return "Smart Agriculture AI is Running 🚀"

# -------------------------------
# 🌱 CROP PREDICTION API
# -------------------------------
@app.route('/predict_crop', methods=['POST'])
def predict_crop():
    data = request.json
    
    N = data['N']
    P = data['P']
    K = data['K']

    prediction = model.predict([[N, P, K]])

    return jsonify({
        'recommended_crop': prediction[0],
        'message': "AI prediction successful ✅"
    })

# -------------------------------
# 🚀 START SERVER WITH NGROK
# -------------------------------
public_url = ngrok.connect(5000)
print("👉 OPEN THIS LINK:", public_url)

def run():
    app.run()

threading.Thread(target=run).start()
