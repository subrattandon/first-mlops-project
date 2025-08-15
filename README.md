🩺 Diabetes Prediction Model – Your First MLOps Project (FastAPI + Docker + K8s)

This project demonstrates Building and Deploying an ML Model using a simple and real-world use case: predicting whether a person is diabetic based on health metrics. The workflow covers:
✅ Model Training
✅ Building the Model locally
✅ API Deployment with FastAPI
✅ Dockerization
✅ Kubernetes Deployment

📊 Problem Statement
Predict if a person is diabetic based on:
Pregnancies
Glucose
Blood Pressure
BMI
Age


We use a Random Forest Classifier trained on the Pima Indians Diabetes Dataset.
🚀 Quick Start
1. Clone the Repo
git clone <your-repo-url>
cd first-mlops-project

2. Create Virtual Environment
python3 -m venv .mlops
source .mlops/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Train the Model
python train.py

5. Run the API Locally
uvicorn main:app --reload
Sample Input for /predict
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 70,
  "BMI": 28.5,
  "Age": 45
}

🐳 Dockerize the API
Build the Docker Image
docker build -t diabetes-prediction-model .
Run the Container
docker run -p 8000:8000 diabetes-prediction-model

☸ Deploy to Kubernetes
kubectl apply -f diabetes-prediction-model-deployment.yaml
