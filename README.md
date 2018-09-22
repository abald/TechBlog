# Установка 

* cd TechBlog
* python3 -m venv myvenv
* myvenv\Scripts\activate - windows
* source myvenv/bin/activate  - linux
* (myvenv) ~$ python3 -m pip install --upgrade pip
* (myvenv) ~$ pip install django
* python manage.py makemigrations blog

##Запуск

* myvenv\Scripts\activate - windows
* source myvenv/bin/activate  - linux
* (myvenv) ~$ python manage.py runserver
