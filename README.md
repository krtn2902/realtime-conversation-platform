#### Video Tutorial for this project
https://youtu.be/SQ4A7Q6_md8

#### Getting the files
Download zip file<br> 
or <br>
git clone command (need git to be installed) and remove git folder afterwards
```
git clone https://github.com/andyjud/django-starter.git . && rm -rf .git
```

## Setup

#### - Create Virtual Environment
###### # Mac
```
python3 -m venv venv
source venv/bin/activate
```
###### # Windows
```
python3 -m venv venv
.\venv\Scripts\activate.bat
```
#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```
#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

#### - Run application
```
python manage.py runserver
```

#### - Generate Secret Key ( ! Important for deployment ! )
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```
---
### instructions for running the code --

download whatever modules that are not defined, 
```
python -m pip install -U 'channels[daphne]'
```

this is what is being done --
https://channels.readthedocs.io/en/latest/deploying.html

Open docker desktop and run --
```
docker run --rm -p 6379:6379 redis:7
```
then open 2 seperate terminals, run the following command --
```
daphne -p 8000 a_core.asgi:application
```
```
daphne -p 8001 a_core.asgi:application
```

In your browser, open 127.0.0.1:8000/ and 127.0.0.1:8001/ to run the 2 separate instances


