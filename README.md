# Password Generator

## Sumário

- [Password Generator](#password-generator)
  - [Sumário](#sumário)
  - [Requisitos](#requisitos)
  - [*Design*](#design)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Ferramentas Utilizadas](#ferramentas-utilizadas)
  - [Execução do Projeto (*Docker Compose*)](#execução-do-projeto-docker-compose)

## Requisitos

1. Sistema gera senha aleatória baseada em políticas de complexidade (tipo de caracteres, números, letras, tamanho, etc);
    - Exemplo: o usuário ao clicar no botão "Gerar Senha" irá obter uma senha aleatória;
2. Usuário irá especificar quantas vezes a senha gerada poderá ser vista e qual o tempo que a senha ficará válida;
    - Exemplo: o usuário irá especificar que a senha possa ser vista apenas duas vezes pelo prazo de um dia;
3. O sistema irá gerar uma URL que dá acesso a visualização da senha, baseando-se nos critérios do item 02;
    - Exemplo: o usuário enviará a URL para que o cliente possa visualizar a senha;
4. Após atingir a quantidade de visualizações ou o tempo disponível, o sistema bloqueia/elimina a visualização da senha (expirado). A senha não deve ser armazenada após sua expiração.

## *Design*

<!-- Explicar os tópicos propostos da aplicação -->

## Estrutura do Projeto

```bash
.
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
├── requirements.txt
├── setup.py
├── src
│   ├── frontend
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── forms.py
│   │   ├── helpers.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── base.css
│   │   │   └── js
│   │   │       ├── index.js
│   │   │       └── new_password.js
│   │   └── templates
│   │       ├── base.html
│   │       ├── index.html
│   │       └── new_password.html
│   └── password_generator
│       ├── __init__.py
│       ├── config.py
│       ├── helpers.py
│       ├── models.py
│       ├── tasks.py
│       ├── urls.py
│       └── views.py
└── startup.sh

7 directories, 24 files
```

## Tecnologias Utilizadas

- Python 3.8
- Jinja2, HTML5, CSS3, Javascript
- Flask 2.0.2
- MongoDB *latest*
- Docker 20.10.11
- Docker Compose 1.29.2

## Ferramentas Utilizadas

- _Windows 10_
- _Ubuntu 20.04 LTS (WSL2)_
- _Visual Studio Code_

## Execução do Projeto (*Docker Compose*)

Gerar o _build_ do projeto a partir do arquivo _docker-compose.yml_:

```sh
    docker-compose build
```

Iniciar os containers do _MongoDB_, _Backend_ e _Frontend_ de forma desacoplada:

```sh
    # No Linux
    chmod +x startup.sh
    bash startup.sh

    # Em outros SOs
    docker-compose up -d
```

O *frontend* estará disponível em [http://localhost/](http://localhost/).

Para a API de senhas utilizar [http://localhost:5000/passwords/](http://localhost:5000/passwords/).
