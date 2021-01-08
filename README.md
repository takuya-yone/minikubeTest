# minikubeTest
try minikube

### script
```
minikube start --vm=true
minikube start
minikube addons enable ingress
minikube addons enable ingress-dns
minikube addons enable metrics-server
minikube addons enable dashboard
kubectl apply -f yamls/nginx-deployment.yaml
kubectl apply -f yamls/nginx-service.yaml
kubectl apply -f yamls/nginx-ingress.yaml
```

### cleanup
```
kubectl delete deployment nginx-deployment
kubectl delete service nginx-service
kubectl delete ingress nginx-ingress
```
