🛠️ Controle de Estoque - Oficina Mecânica Precision
Este é um sistema web simples desenvolvido com Django para controle de estoque de peças automotivas, feito como parte de um projeto acadêmico. O objetivo é resolver o problema de controle manual de itens como filtros de óleo, pastilhas de freio e velas, evitando faltas ou excessos no estoque da oficina.

📌 Funcionalidades
Cadastro de Itens : Permite registrar peças com nome, código de referência, quantidade, localização, e estoque mínimo.
Painel de Estoque : Lista todas as peças cadastradas com destaque visual para aquelas abaixo do estoque mínimo.
Movimentação de Estoque : Interface para registrar entradas (reposição) e saídas (uso) de peças.
🚀 Tecnologias Utilizadas
Python 3.x
Django 5.x
SQLite (banco de dados padrão)
HTML/CSS (modelos)
📁 Estrutura básica do projeto

oficina/ ├── estoque/ │ ├── admin.py │ ├── models.py │ ├── views.py │ ├── templates/ │ └── ... ├── oficina/ │ ├── settings.py │ └── urls.py ├── db.sqlite3 ├── manage.py └── requisitos.txt
