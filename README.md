# Django Setup

## Local development
- How to
### Create a new virtual environment
```
sudo apt install virtualenv
virtualenv myenv -p python3
cd myenv
source bin/activate
```

### Clone the repo
```
mkdir gitrepo
cd gitrepo
git init
git pull

pip install -r requirements.txt
```

### Start the webserver
```
python manage.py runserver
```
You are all set for local development

# Frontend
- The template (main.html) is [here](homepage/templates/homepage/)
  - once you clone and run the server, you can start building using the template
  
# Elasticsearch Dependencies
### Install JDK 8
```
sudo apt update
sudo apt install apt-transport-https
sudo apt install openjdk-8-jdk
```
### Install Elasticsearch
```
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
sudo apt update
sudo apt install elasticsearch
```
### Enable service
```
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service

```
### Check status
```
curl -X GET "localhost:9200/"
```

### On Success

```

{
  "name" : "kwEpA2Q",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "B-5B34LXQFqDeIYwSgD3ww",
  "version" : {
    "number" : "7.0.0",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "b7e28a7",
    "build_date" : "2019-04-05T22:55:32.697037Z",
    "build_snapshot" : false,
    "lucene_version" : "8.0.0",
    "minimum_wire_compatibility_version" : "6.7.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}

```

