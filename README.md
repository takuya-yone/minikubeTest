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

### enable minikube service
```
minikube tunnel
minikube dashboard
```

### create service
```
kubectl apply -f yamls/nginx

kubectl apply -f yamls/python

kubectl apply -f yamls/redis

kubectl apply -f yamls/traefik

kubectl apply -f yamls/prometheus

kubectl apply -f yamls/grafana

kubectl apply -f yamls/local-ingress.yaml


```
### cleanup
```
kubectl delete ingress local-ingress

kubectl delete service nginx-service
kubectl delete deployment nginx-dep

kubectl delete service python-service
kubectl delete deployment python-dep

kubectl delete service redis-service
kubectl delete deployment redis-dep

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
docker-compose up -d --build
docker-compose down
docker build -f ../build/Dockerfile -t test-python:latest
```


### for Rancher
```
#!/bin/bash
sudo yum update -y
sudo yum install docker git -y
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker
sudo systemctl start docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
curl https://raw.githubusercontent.com/jesseduffield/lazydocker/master/scripts/install_update_linux.sh | bash
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
sudo mv kubectl /usr/local/bin/kubectl
sudo chmod +x /usr/local/bin/kubectl
echo 'source <(kubectl completion bash)' >>~/.bashrc
kubectl completion bash > kubectl-completer
sudo kubectl completion bash >/etc/bash_completion.d/kubectl
sudo mv kubectl-completer /etc/bash_completion.d/kubectl-completer
echo 'alias k=kubectl' >>~/.bashrc
echo 'complete -F __start_kubectl k' >>~/.bashrc
git clone https://github.com/takuya-yone/minikubeTest.git
docker pull rancher/rancher
docker pull rancher/rancher-agent:v2.6.2

# for Master
sudo systemctl start docker
sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher
```