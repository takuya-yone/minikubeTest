# minikubeTest
try minikube

### script
```
minikube start --vm=true
minikube addons enable ingress
minikube addons enable metrics-server
minikube addons enable dashboard
kubectl apply -f https://k8s.io/examples/application/deployment.yaml
kubectl expose deployment nginx-deployment --type=NodePort --name=nginx-service
```