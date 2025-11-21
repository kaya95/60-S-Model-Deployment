<img width="1920" height="1080" alt="Screenshot 2025-11-18 135744" src="https://github.com/user-attachments/assets/f541ccba-bc10-4d02-b432-0bd091c6bdb8" />
<img width="1920" height="1080" alt="Screenshot 2025-11-18 142750" src="https://github.com/user-attachments/assets/e6858345-2d3f-42f9-b248-dfd47c71e066" />
<img width="1920" height="1080" alt="Screenshot 2025-11-18 142924" src="https://github.com/user-attachments/assets/cf121e85-03a6-42a0-b0ea-54b13df023f1" />
GPU Cost Guardian – 60-Second Model Deployment Demo

A lightweight, production-ready example of an ML deployment using Docker + FastAPI.
This project demonstrates how to take a Python ML script, containerize it, expose a clean REST API, and test it locally — all in under 60 seconds.

The purpose of this repository is to show real MLOps deployment skills in a clean, simple, professional GitHub project.

📌 Features

✔ FastAPI production server
✔ Docker containerization
✔ /predict REST endpoint
✔ Real working ML inference script
✔ JSON request/response format
✔ Fully local testing (no cloud needed)
✔ Lightweight & easy to run
✔ Perfect for MLOps portfolio projects

🚀 Quick Start
1. Clone the repo
git clone https://github.com/<your_username>/<repo_name>.git
cd <repo_name>

2. Build Docker Image
docker build -t model-60s .

3. Run the container
docker run -d -p 8000:8000 --name model60s model-60s

4. Test the API
Using curl:
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d "{\"features\": [3.0,5.0,4.0,4.5,4.8]}"

Example response:
{
  "fraud_probability": 4.26,
  "is_fraud": true,
  "confidence": 1.0
}

📁 Project Structure
📦 project
│
├── deploy_60s.py          # Main FastAPI inference server
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build file
├── test_instructions.txt   # Manual test instructions
├── render.yaml             # Optional cloud deployment config
├── screenshots/            # UI + test screenshots
└── README.md               # (this file)

🧠 How It Works
1️⃣ Client sends JSON
{"features": [value1, value2, ...]}

2️⃣ API loads the model logic inside Docker

The file deploy_60s.py contains:

Model loading

Prediction logic

Probability output

Fraud rule decision logic

3️⃣ Response returned

The API returns:

fraud_probability

binary fraud decision

confidence score

🧪 Testing

Use your browser:

http://localhost:8000/docs


FastAPI auto-generates an interactive Swagger UI for you to test the /predict endpoint.

🐳 Docker Overview
Build image
docker build -t model-60s .

Run container
docker run -d -p 8000:8000 model-60s

Stop container
docker stop model60s

Remove container
docker rm model60s

📈 Architecture Diagram
Client → FastAPI → Model Logic → Response JSON
           │
        Docker

📝 Future Improvements (Optional)

These are optional upgrades you can implement later:

Add real trained ML model (sklearn, XGBoost, etc.)

Add logging + monitoring (Prometheus, Grafana)

Add request validation

Add model versioning endpoint

CI/CD GitHub Actions pipeline

Add cloud deployment (Render/AWS/GCP)

Add authentication token

Add GPU/CPU resource metrics

📄 License

MIT License.

👤 Author


Built by kaya — demonstrating real, hands-on MLOps deployment skills.
