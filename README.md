# Install

TechBlog works in virtual environment.

## Make virtualenv and install requirements

### Windows

```
python3 -m venv env
env\Scripts\activate
pip install django==2.1.2
```

### Linux

```bash
virtualenv -p python3.6 env
source env/bin/activate
pip install django==2.1.2
```

### Mac

Install [Homebrew](https://brew.sh)

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```bash
brew install python
```

If you encounter permission errors, try these steps:

```bash
sudo chown -R "$USER":admin /usr/local
sudo chown -R "$USER":admin /Library/Caches/Homebrew
```

Now check Python version, it should return `Python 3.6`+:

```bash
python3 -V
```

Next steps install `pip`, `virtualenv` (and activates it) and `django 2.1.2`:

```bash
sudo easy_install pip
sudo pip install virtualenv
virtualenv env -p python3.6
source env/bin/activate
pip install django==2.1.2
```

## Make database migrations

```bash
python3 manage.py migrate
```

## Create a superuser

```
python3 manage.py createsuperuser
```

# Start

```
python3 manage.py runserver
```

Service should be available at localhost port 8000: `http://127.0.0.1:8000/`
