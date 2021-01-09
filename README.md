# minikubeTest
try minikube

### setup
```
minikube start
minikube start --vm=true 
minikube addons enable ingress
minikube addons enable ingress-dns
minikube addons enable metrics-server
minikube addons enable dashboard
```

### create service
```
kubectl apply -f yamls/test-deployment.yaml
kubectl apply -f yamls/test-service.yaml
kubectl apply -f yamls/test-ingress.yaml
```
### cleanup
```
kubectl delete deployment test-deployment
kubectl delete service test-service
kubectl delete ingress test-ingress
```

### create docker image
```
docker build -f ../docker/Dockerfile -t test-python:latest
```