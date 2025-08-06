# 📈 StockSight AI – Real-time Stock Price Predictor

A modern, scalable, and GitOps-powered application that predicts and displays real-time stock prices using FastAPI, Docker, Kubernetes, and Argo CD.

---

## 🚀 Features

- ⚡ FastAPI backend for high-performance asynchronous API
- 🔍 Real-time stock price fetching via `yfinance`
- 📦 Dockerized for consistent development and production
- ☸️ Kubernetes manifests for scalable deployment
- 🔄 GitOps CI/CD powered by Argo CD
- 🎨 Minimal HTML/CSS UI for clean, responsive interface
- 🧪 Fully containerized and Minikube/K8s ready

---

## 📂 Project Structure

stock-price-app/
├── app/
│ ├── main.py # FastAPI app code
│ ├── requirements.txt # Python dependencies
│ ├── templates/
│ │ └── index.html # Frontend template
├── Dockerfile
├── k8s/
│ ├── deployment.yaml # Kubernetes Deployment
│ ├── service.yaml # Kubernetes Service (NodePort)
│ └── argocd.yaml # Argo CD Application manifest
├── README.md


---

## 🛠️ Tech Stack

| Layer        | Tooling                  |
|--------------|---------------------------|
| Backend API  | FastAPI (Python)          |
| Data Fetch   | `yfinance`                |
| Container    | Docker                    |
| Deployment   | Kubernetes (Minikube)     |
| GitOps CD    | Argo CD                   |

---

## 📦 Setup Instructions
git clone 
cd Gitops-StockSight-AI-

✅ 2. Run Locally with Docker
docker build -t stock-price-app .
docker run -p 5000:5000 stock-price-app
Access the app: http://localhost:5000

☸️ Deploy to Minikube (Kubernetes)
🔹 1. Start Minikube
minikube start

🔹 2. Deploy the App
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

🔹 3. Access the App
minikube service stock-price-service

🔄 Argo CD Setup (GitOps)
📥 Install Argo CD CLI
curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
chmod +x argocd
sudo mv argocd /usr/local/bin/

🚀 Port Forward Argo CD UI
kubectl port-forward svc/argocd-server -n argocd 8080:443
Visit: https://localhost:8080

Default login:
Username: admin
Password: run this:
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d
🧠 Apply Argo CD App
kubectl apply -f k8s/argocd.yaml
🌐 Live App Screenshot

🙌 Author
HARSHITHA G M – DevOps Enthusiast | AI + Cloud | 🚀

📄 License
This project is licensed under the MIT License.


