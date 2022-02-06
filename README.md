# Tianjun Mo's Demo Project
In this project, I built a containerized service and set up a CI/CD workflow to automatically deploy to Cloud Run on Google Cloud Platform. 
Demo Link: http://cloud.tinchun.top   
## Deployment
### Kubernetes
We can deploy this project to a Kubernetes cluster with:
```bash
kubectl apply -f https://raw.githubusercontent.com/motianjun4/fastapi/master/kubernetes-deployment.yaml

# or clone the repository

kubectl apply -f ./kubernetes-deployment.yaml
```

### IaC (Infrastrcture as Code)
In this project, I used Terraform to automatically deploy my CI/CD workflow and service to GCP.  
This includes two steps:
1. Create a Cloud Build trigger for CI/CD
2. Create a Cloud Run resource to deploy this service.  
Check [main.tf](./main.tf) for more details.  

To deploy this project to GCP, simply: 
1. Clone this repository to the [Cloud Shell](https://cloud.google.com/shell),
2. Modify the [terraform.tfvars](./terraform.tfvars) file,
3. Use `terraform init` and `terraform apply` to deploy it.
### Docker
If you want to deploy this project, just:
``` bash
docker pull ghcr.io/motianjun4/fastapi:master
docker run -p 8000:8000 ghcr.io/motianjun4/fastapi:master
```

then you can visit http://localhost:8000/  

## Development
You can setup the development environment on docker or on local machine.

### Prerequisites:
1. Python 3

```bash
$ git clone https://github.com/motianjun4/fastapi.git
$ cd fastapi

# Optional: set up Python Virtual Environment

# Install dependencies
$ make install

# Run Development Server
$ make run

```
