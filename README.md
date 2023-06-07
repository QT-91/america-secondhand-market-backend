# ASM Backend

### America Secondhand Market Backend
### python 3.10.11, [django](https://www.djangoproject.com/) 4.2.1, [wagtail](https://wagtail.org/) 5.0.1

---

## Getting Started

You can use Virtual Environment, [which is included in Python.](https://www.w3schools.com/django/django_create_virtual_environment.php) or use [Anaconda](https://www.anaconda.com/) before install required python packages


```
pip install -r requirements.txt
```

---
### DB setting 

if you are a biginner, it's better to use [SQLite](https://www.sqlite.org/index.html) instead of [MySQL](https://www.mysql.com/). Edit [this file](!asm_backend/settings/base.py) like this.

### SQLite (Default Django DB)
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
```


### MySQL (Project DB)

#### [(this guide will help you)](https://losskatsu.github.io/it-infra/mysql-install-mac/#)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_django_db',
        'USER': 'my_database_user',
        'PASSWORD': 'my_database_password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```
or you can use ./my.cnf file
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "./my.cnf",
        },
    }
}
```

before running the server,
```
mysql.server start
```

---

### Running Server

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```