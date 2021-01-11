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
kubectl apply -f yamls/nginx

kubectl apply -f yamls/python

kubectl apply -f yamls/traefik

kubectl apply -f yamls/prometheus

kubectl apply -f yamls/grafana

kubectl apply -f yamls/local-ingress.yaml

minikube tunnel
minikube dashboard
```
### cleanup
```
kubectl delete ingress local-ingress

kubectl delete service nginx-service
kubectl delete deployment nginx-dep

kubectl delete service python-service
kubectl delete deployment python-dep

kubectl delete service grafana-service
kubectl delete deployment grafana-dep

kubectl delete service prometheus-service
kubectl delete deployment prometheus-dep

kubectl delete service traefik-service
kubectl delete deployment traefik-dep
kubectl delete serviceaccounts traefik-ingress-controller
kubectl delete clusterrole traefik-ingress-controller
kubectl delete clusterrolebindings traefik-ingress-controller
```
### create docker image
```
docker build -f ../docker/Dockerfile -t test-python:latest
```