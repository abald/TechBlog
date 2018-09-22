# Install 

TechBlog works in virtual environment.

**Make virtualenv and install requirements**

On Windows
```
python3 -m venv env
env\Scripts\activate
pip install django~=1.11.0
```

On Linux
```bash
virtualenv -p python3.6 env
source env/bin/activate
pip install django~=1.11.0
```

**Make database migrations**

On Windows
```
* python3 manage.py makemigrations blog
```

On Linux
```bash
* python3 manage.py makemigrations blog
```

# Start

```
python3 manage.py runserver
```