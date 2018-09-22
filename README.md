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

# Start

```
python3 manage.py runserver
```