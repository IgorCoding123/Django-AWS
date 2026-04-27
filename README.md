# ☁️ CarCloud - Gestão de Veículos com Django & AWS

Bem-vindo ao **CarCloud**, um sistema que desenvolvi para demonstrar a integração de uma aplicação **Django** com o ecossistema da **AWS**. O foco aqui foi criar algo robusto, utilizando **RDS (PostgreSQL)** para os dados e **S3** para o armazenamento de mídia, garantindo escalabilidade e segurança.

---

## 🏎️ O Projeto

O CarCloud é uma vitrine de veículos premium. A ideia foi unir um design moderno (Dark Mode com Glassmorphism) a uma infraestrutura de nuvem real. Nada de banco de dados local ou arquivos salvos no servidor; tudo aqui respira Cloud Computing.

### 🏗️ Arquitetura
O sistema funciona da seguinte forma:
1. **Frontend:** Desenvolvido com Django Templates e Bootstrap 5 customizado.
2. **Backend:** Core em Django 6, gerenciando a lógica de negócios e integração.
3. **Database:** Banco de dados **PostgreSQL** hospedado no **Amazon RDS**.
4. **Storage:** Fotos dos veículos enviadas automaticamente para o **Amazon S3** via `django-storages`.

---

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Framework:** Django 6.x
*   **Banco de Dados:** AWS RDS (PostgreSQL)
*   **Armazenamento:** Amazon S3
*   **Segurança:** Variáveis de ambiente com `python-dotenv`
*   **Estilização:** CSS Customizado + Bootstrap 5

---

## ⚙️ Como Rodar o Projeto

Se você quiser clonar este projeto e testar na sua própria conta AWS, siga estes passos:

### 1. Dependências
```bash
pip install -r requirements.txt
```

### 2. Configuração da Nuvem (.env)
Você precisará criar um arquivo `.env` na raiz do projeto seguindo este modelo:
```env
# Django
SECRET_KEY=sua_secret_key_aqui
DEBUG=True

# AWS Credentials
AWS_ACCESS_KEY_ID=sua_access_key
AWS_SECRET_ACCESS_KEY=sua_secret_key
AWS_STORAGE_BUCKET_NAME=nome-do-seu-bucket
AWS_S3_REGION_NAME=us-east-2

# Database (RDS)
DB_NAME=carcloud_db
DB_USER=postgres
DB_PASSWORD=sua_senha_do_rds
DB_HOST=seu-endpoint-do-rds.amazonaws.com
DB_PORT=5432
```

### 3. Migrações e Execução
```bash
python manage.py migrate
python manage.py runserver
```

---

## 📸 Screenshots
*(Dica: Aqui você pode adicionar os prints que tirou do seu projeto funcionando!)*

---

## 🚀 Desafios Superados
Neste projeto, o maior aprendizado foi lidar com as permissões de acesso da AWS (IAM Policies e Bucket Policies) e configurar a assinatura **S3V4** para a região de Ohio, garantindo que o upload de arquivos fosse seguro e performático.

---
Desenvolvido por **Igor Coding**.
