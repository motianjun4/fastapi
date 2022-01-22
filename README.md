# My Playground
Hi everyone, this is my playground.  
I built this containerized service and set up a CI/CD workflow to automatically deploy to Cloud Run on Google Cloud Platform.  
Demo Link: https://motianjun4.github.io/fastapi or http://cloud.tinchun.top 
Hope you all like this project!!  
## Deployment
If you want to deploy this project, just:
### Prerequisites:
1. Docker 

``` bash
docker run -p 8000:8000 ghcr.io/motianjun4/fastapi:master
```

then you can 

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
then, you can 