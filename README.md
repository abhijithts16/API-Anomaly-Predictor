# Anomaly Predictor — Middleware API Security with Machine Learning

A middleware-based API security solution that integrates **machine learning models** into a Flask application for real-time anomaly detection in API traffic.  
Supports both **UI-based** and **bulk JSON API** predictions.

---

## Features
- **One-Class SVM** — trained on normal API behaviour for unlabelled data anomaly detection.
- **Tuned OCSVM** — optimised with GridSearchCV to reduce false positives.
- **Hybrid Random Forest** — supervised model for datasets with labelled anomalies.
- **Flask Integration** — model selection via UI or API.
- **Bulk Testing** — run multiple JSON predictions automatically using batch script.
- **Bearer Token Security** — for API endpoint `/predict_json`.

---

## Folder Structure
```
anomalyPredictorModels.ipynb   # Model training & export
ocsvm_model.pkl                # Trained One-Class SVM model
hybrid_model.pkl               # Trained Hybrid Random Forest model
scaler.pkl                     # StandardScaler for preprocessing
App.py                         # Flask application
templates/                     # UI HTML files
json_requests.py               # Bulk testing JSON requests
run_json_requests.bat          # Batch script for automated bulk testing
supervised_dataset.csv         # Dataset sample
```

---

## Installation & Usage

### 1. Install dependencies  
**For Notebook training:**
```bash
pip install notebook pandas numpy scikit-learn joblib
```

**For Flask app:**
```bash
pip install flask pandas numpy scikit-learn joblib requests
```

### 2. Run Flask app
```bash
python App.py
```
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 3. Bulk Testing
```bash
python json_requests.py
```
Or run:
```bash
run_json_requests.bat
```

---

## Dataset
- **Source:** [API Access Behaviour Anomaly Dataset - Kaggle](https://www.kaggle.com/datasets/tangodelta/api-access-behaviour-anomaly-dataset)  
- Contains features like API access duration, uniqueness, session stats, and binary anomaly labels.

---
