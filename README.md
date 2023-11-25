# Como inicar o projeto django

## Inicializando e ativando ambiente virtual

```bash
# Criando ambiente
python -m venv env

# Ativando no Linux
source env/bin/activate

# Ativando no Windows
.\env\scripts\activate
```

## Instalando dependencias

```bash
pip install django

# Opcional

pip install django-jazzmin
```

## Iniciando projeto Django

```bash
django-admin startproject <nome-do-seu-site>
```

## Estrutura de arquivos

```bash
<nome-do-seu-site>/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### Entendendo manage.py

- manage.py: É um command-line que permite a interação com o projeto Django de várias formas. Vocês podem encontrar mais informação nessa página da documentação [django-admin and manage.py](https://docs.djangoproject.com/en/4.2/ref/django-admin/).
- Rodando o interpretador do python o modulo `manage.py` vemos a lista de comandos que ele aceita.

```bash
# Stdin (entrada)
➜ python app/manage.py


# Stdout (saida)

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```

### Como é a organização padrao de projetos django

Separamos cada parte do nosso projeto no que chamam de _apps_.\
Cada _app_ é um braço de nossa aplicação.\
Para inciar um app:

```bash
python manage.py startapp <nome-do-app>
```

Resulta na criação da estrutura abaixo:

```bash
<nome-do-app>/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
