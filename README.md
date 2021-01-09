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
kubectl apply -f yamls/nginx/nginx-deployment.yaml
kubectl apply -f yamls/nginx/nginx-service.yaml

kubectl apply -f yamls/python/python-deployment.yaml
kubectl apply -f yamls/python/python-service.yaml

kubectl apply -f yamls/local-ingress.yaml
```
### cleanup
```
kubectl delete ingress local-ingress
kubectl delete service nginx-service
kubectl delete service python-service
kubectl delete deployment nginx-deployment
kubectl delete deployment python-deployment
```
### create docker image
```
docker build -f ../docker/Dockerfile -t test-python:latest
```