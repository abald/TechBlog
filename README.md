# Install 

TechBlog works in virtual environment.

**Make virtualenv and install requirements**

On Windows
```
python3 -m venv env
env\Scripts\activate
pip install django==2.1.1
```

On Linux
```bash
virtualenv -p python3.6 env
source env/bin/activate
pip install django==2.1.1
```

**Make database migrations**

```
* python3 manage.py migrate
```

**Make superuser**

```
python3 manage.py createsuperuser
```

# Start

```
python3 manage.py runserver
```
Service ready and could be accessed trought `http://127.0.0.1:8000/`