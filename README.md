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
