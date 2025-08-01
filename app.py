from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__) # This line correctly sets up Flask for static files
# ... rest of your app.py code ...
app = Flask(__name__)

# Load the trained model
# Ensure 'churn_model.pkl' is in the same directory as app.py
try:
    model = joblib.load('churn_model.pkl')
    print("Churn prediction model loaded successfully.")
except FileNotFoundError:
    print("Error: churn_model.pkl not found. Please run model_trainer.py first.")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please train the model first.'}), 500

    try:
        data = request.json
        # Extract features from the request data
        # Ensure these match the features used for training
        features = pd.DataFrame([data])

        # Make prediction
        churn_probability = model.predict_proba(features)[:, 1][0] # Probability of being churned (class 1)
        prediction = model.predict(features)[0]

        status = "High Churn Risk" if prediction == 1 else "Low Churn Risk"

        return jsonify({
            'customer_id': data.get('customer_id', 'N/A'),
            'churn_probability': f"{churn_probability:.2f}",
            'prediction_status': status
        })
    except Exception as e:
        return jsonify({'error': str(e), 'details': 'Ensure all required features are provided and in the correct format (e.g., numbers for numerical, strings for categorical).'}), 400

if __name__ == '__main__':
    # Ensure the model file exists before running the app
    if not os.path.exists('churn_model.pkl'):
        print("Model file 'churn_model.pkl' not found. Please run 'python model_trainer.py' first.")
    else:
        app.run(debug=True) # debug=True restarts server on code changes