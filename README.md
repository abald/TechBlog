# Установка 

* (inline) cd TechBlog
* (inline) python3 -m venv myvenv
* (inline) myvenv\Scripts\activate - windows
* (inline) source myvenv/bin/activate  - linux
* (inline) (myvenv) ~$ python3 -m pip install --upgrade pip
* (inline) (myvenv) ~$ pip install django~=1.11.0
* (inline) python3 manage.py makemigrations blog

# Запуск

* (inline) myvenv\Scripts\activate - windows
* (inline) source myvenv/bin/activate  - linux
* (inline) (myvenv) ~$ python3 manage.py runserver
