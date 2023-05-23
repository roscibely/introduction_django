# Começando com Django 

## Introdução

Este é um tutorial de introdução ao Django, um framework para desenvolvimento web em Python.

## Pré-requisitos

Para seguir este tutorial, você precisa ter o Python 3 instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

## Instalação

Para instalar o Django, você pode usar o gerenciador de pacotes do Python, o pip. Para isso, basta executar o seguinte comando:

```bash
pip install django
```

## Criando um projeto

Para criar um projeto Django, basta executar o seguinte comando:

```bash
django-admin startproject hellodjango
```

O comando acima irá criar uma pasta chamada `hellodjango` com a seguinte estrutura:

```bash
hellodjango/
    manage.py
    hellodjango/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

A pasta `hellodjango` é o diretório raiz do seu projeto. O arquivo `manage.py` é um utilitário que permite interagir com o projeto de diversas formas. A pasta `hellodjango` é o pacote Python do seu projeto. O arquivo `settings.py` contém as configurações do seu projeto. O arquivo `urls.py` contém as configurações de roteamento do seu projeto. O arquivo `wsgi.py` é um ponto de entrada para servidores web compatíveis com WSGI, como o Gunicorn.

## Rodando o servidor

Para rodar o servidor de desenvolvimento do Django, basta executar o seguinte comando:

```bash
python manage.py runserver
```

O servidor irá rodar na porta 8000 por padrão. Para rodar na porta 8080, por exemplo, basta executar o seguinte comando:

```bash
python manage.py runserver 8080
```

## Criando um superusuário

Para criar um superusuário, basta executar o seguinte comando:

```bash
python manage.py createsuperuser
```

O comando acima irá criar um superusuário para o Django Admin.

## Criando banco de dados

Para criar o banco de dados, basta executar o seguinte comando:

```bash
python manage.py migrate
```

O comando acima irá criar o banco de dados do seu projeto.


## Criando uma aplicação

Para criar uma aplicação Django, basta executar o seguinte comando:

```bash
python manage.py startapp homepage
```

O comando acima irá criar uma pasta chamada `homepage` com a seguinte estrutura:

```bash
homepage/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

A pasta `homepage` é o pacote Python da sua aplicação. O arquivo `admin.py` contém as configurações do Django Admin para a sua aplicação. O arquivo `apps.py` contém as configurações da sua aplicação. A pasta `migrations` contém as migrações do seu projeto. O arquivo `models.py` contém os modelos do seu projeto. O arquivo `tests.py` contém os testes da sua aplicação. O arquivo `views.py` contém as views da sua aplicação.

Precisamos criar o template da aplicação. Para isso, basta criar uma pasta chamada `templates` dentro da pasta da aplicação. Dentro da pasta `templates`, crie uma pasta com o nome da sua aplicação. Dentro da pasta da sua aplicação, crie um arquivo chamado `index.html`. O arquivo `index.html` será o template da sua aplicação.

No arquivo `index.html`
    
```html
    <!DOCTYPE html>

    <h1> My first Django app </h1>
    <p> Hello, world!</p>
```

Precisamos criar a view da aplicação. Para isso, basta abrir o arquivo `views.py` e adicionar o seguinte código:

```python
from django.views.generic import TemplateView

class HomepageView(TemplateView): 
    template_name = 'index.html'

```

Para executar o projeto, basta rodar o servidor de desenvolvimento do Django e acessar a URL `http://localhost:8000/`.



```bash
python manage.py runserver
```




