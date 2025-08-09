
import requests
import json

url = "http://127.0.0.1:5000/predict_json"
headers = {
    "Authorization": "Bearer demo-bearer-token-abc123",
    "Content-Type": "application/json"
}

inputs = [
    {
        "inter_api_access_duration": 0.0001, "api_access_uniqueness": 0.01, "sequence_length": 20,
        "vsession_duration": 250, "num_sessions": 150, "num_users": 100, "num_unique_apis": 30,
        "ip_type_default": 1, "source_F": 0, "model_type": "ocsvm"
    },
    {
        "inter_api_access_duration": 0.00725, "api_access_uniqueness": 1.0, "sequence_length": 2.0,
        "vsession_duration": 1, "num_sessions": 2, "num_users": 1, "num_unique_apis": 2,
        "ip_type_default": 0, "source_F": 0, "model_type": "hybrid"
    },
    {
        "inter_api_access_duration": 0.001, "api_access_uniqueness": 0.02, "sequence_length": 50,
        "vsession_duration": 400, "num_sessions": 90, "num_users": 70, "num_unique_apis": 35,
        "ip_type_default": 1, "source_F": 1, "model_type": "ocsvm"
    },
    {
        "inter_api_access_duration": 0.009, "api_access_uniqueness": 0.9, "sequence_length": 3,
        "vsession_duration": 5, "num_sessions": 1, "num_users": 1, "num_unique_apis": 1,
        "ip_type_default": 0, "source_F": 0, "model_type": "hybrid"
    },
    {
        "inter_api_access_duration": 0.0004, "api_access_uniqueness": 0.01, "sequence_length": 80,
        "vsession_duration": 600, "num_sessions": 100, "num_users": 90, "num_unique_apis": 40,
        "ip_type_default": 1, "source_F": 1, "model_type": "ocsvm"
    },
    {
        "inter_api_access_duration": 0.0003, "api_access_uniqueness": 0.015, "sequence_length": 60,
        "vsession_duration": 300, "num_sessions": 120, "num_users": 80, "num_unique_apis": 25,
        "ip_type_default": 1, "source_F": 0, "model_type": "hybrid"
    },
    {
        "inter_api_access_duration": 0.01, "api_access_uniqueness": 0.95, "sequence_length": 1,
        "vsession_duration": 2, "num_sessions": 1, "num_users": 1, "num_unique_apis": 1,
        "ip_type_default": 0, "source_F": 1, "model_type": "ocsvm"
    },
    {
        "inter_api_access_duration": 0.0002, "api_access_uniqueness": 0.005, "sequence_length": 100,
        "vsession_duration": 800, "num_sessions": 200, "num_users": 150, "num_unique_apis": 60,
        "ip_type_default": 1, "source_F": 0, "model_type": "hybrid"
    },
    {
        "inter_api_access_duration": 0.0005, "api_access_uniqueness": 0.01, "sequence_length": 75,
        "vsession_duration": 350, "num_sessions": 110, "num_users": 95, "num_unique_apis": 33,
        "ip_type_default": 1, "source_F": 1, "model_type": "ocsvm"
    },
    {
        "inter_api_access_duration": 0.008, "api_access_uniqueness": 0.99, "sequence_length": 2,
        "vsession_duration": 3, "num_sessions": 2, "num_users": 1, "num_unique_apis": 1,
        "ip_type_default": 0, "source_F": 0, "model_type": "hybrid"
    }
]

for i, payload in enumerate(inputs, start=1):
    response = requests.post(url, headers=headers, json=payload)
    try:
        print(f"--- Request {i} ---")
        print("Input:", json.dumps(payload, indent=2))
        print("Response:", response.json())
    except Exception as e:
        print(f"Error on request {i}: {e}")
    print()
