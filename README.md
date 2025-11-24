# 🐾 PetVac – Sistema de Gerenciamento de Vacinação de Pets

## 📌 Descrição do Projeto

O **PetVac** é um sistema desenvolvido para auxiliar **clínicas veterinárias** no gerenciamento de:

- Pets
- Tutores
- Usuários internos (veterinários e recepcionistas)
- Vacinas: datas de aplicação, próximas doses e histórico

O sistema foi projetado para uso **exclusivo da clínica**, garantindo que apenas profissionais autorizados tenham acesso às informações.

---

## 🛠️ Tecnologias Utilizadas

- **Python** – Lógica de negócio (backend)
- **Pandas** – Manipulação e persistência de dados em arquivos CSV
- **Streamlit** – Interface web simples, funcional e rápida de desenvolver
- **CSS** – Customização visual das telas
- **CSV** – Armazenamento dos dados:
  - `vacinas.csv`
  - `pets.csv`
  - `tutors.csv`
  - `usuarios.csv`

---

## 🚀 Como Rodar o Projeto Localmente

1. **Clonar o repositório**

bash
git clone <repo-url>
cd PETVAC
   

2. **Criar e ativar o ambiente virtual**

 python -m venv .venv
.venv\Scripts\activate


2. **Instalar as dependências**

pip install -r requirements.txt


3. **Executar o sistema (Streamlit)**

streamlit run app.py

---
## 📂 Estrutura do Projeto

```
PETVAC
├── backend/
│   ├── database.py
│   │     • carregar_dados()
│   │     • salvar_dados()
│   │     • Define as colunas dos arquivos CSV
│   │
│   ├── services.py
│   │     • Funções principais do sistema:
│   │       - cadastrar_pet(), atualizar_pet()
│   │       - cadastrar_tutor(), atualizar_tutor()
│   │       - registrar_vacina()
│   │       - consultar_vacinas_pendentes() ...
│   │
│   ├── tutor.py                         • Classe Tutor
│   ├── pet.py                           • Classe Pet
│   ├── vacina.py                        • Classe Vacina
│   ├── historico_vacinas.py             • Classe HistóricoVacina
│   └── usuario.py                       • Classe Usuário
│
├── data/
│   ├── tutors.csv
│   ├── pets.csv
│   ├── vacinas.csv
│   └── usuarios.csv
│
├── pages/   (interface – páginas do sistema)
│   ├── home.py
│   ├── cadastro_tutor.py
│   ├── cadastro_pet.py
│   ├── vacinas.py
│   ├── historico.py
│   └── cadastrar_usuario.py
│
└── app.py
      • Arquivo principal do sistema  
      • Controla login, cadastro de usuários e navegação entre as páginas
