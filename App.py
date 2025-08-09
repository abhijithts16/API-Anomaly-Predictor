from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load models and scaler
ocsvm_model = joblib.load('ocsvm_model.pkl')
hybrid_model = joblib.load('hybrid_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

# UI-based API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        selected_model = request.form['model_type']
        model = ocsvm_model if selected_model == 'ocsvm' else hybrid_model

        features = [
            float(request.form['inter_api_access_duration']),
            float(request.form['api_access_uniqueness']),
            float(request.form['sequence_length']),
            int(request.form['vsession_duration']),
            int(request.form['num_sessions']),
            int(request.form['num_users']),
            int(request.form['num_unique_apis']),
            bool(int(request.form['ip_type_default'])),
            bool(int(request.form['source_F']))
        ]

        features_np = np.array(features).reshape(1, -1)
        scaled_input = scaler.transform(features_np)
        raw_pred = model.predict(scaled_input)
        prediction = 'normal' if raw_pred[0] == 1 else 'anomaly'

        print(f"Model used: {selected_model}, Prediction: {raw_pred[0]}")
        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

# JSON-based API endpoint
@app.route('/predict_json', methods=['POST'])
def predict_json():
    
    # --- Check Bearer token in Authorization header ---
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({'error': 'Missing or invalid Authorization header'}), 401

    token = auth_header.split(" ")[1]
    if token != "demo-bearer-token-abc123":
        return jsonify({'error': 'Invalid token'}), 403
    
    try:
        data = request.get_json()

        model_choice = data.get('model_type', 'ocsvm')
        model = ocsvm_model if model_choice == 'ocsvm' else hybrid_model

        features = [
            float(data['inter_api_access_duration']),
            float(data['api_access_uniqueness']),
            float(data['sequence_length']),
            int(data['vsession_duration']),
            int(data['num_sessions']),
            int(data['num_users']),
            int(data['num_unique_apis']),
            bool(int(data['ip_type_default'])),
            bool(int(data['source_F']))
        ]

        features_np = np.array(features).reshape(1, -1)
        scaled_input = scaler.transform(features_np)
        raw_pred = model.predict(scaled_input)
        pred_value = int(raw_pred[0])
        prediction = 'normal' if pred_value == 1 else 'anomaly'

        return jsonify({
            'prediction': prediction,
            'model_used': model_choice,
            'raw_prediction': pred_value
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
