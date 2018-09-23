# Установка 

```
* cd TechBlog
* python3 -m venv myvenv
* myvenv\Scripts\activate - windows
* source myvenv/bin/activate  - linux
* (myvenv) ~$ python3 -m pip install --upgrade pip
* (myvenv) ~$ pip install django~=1.11.0
* python3 manage.py makemigrations blog
* python manage.py createsuperuser
```

# Запуск

```
* myvenv\Scripts\activate - windows
* source myvenv/bin/activate  - linux
* (myvenv) ~$ python3 manage.py runserver
```