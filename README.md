🐾 PetVac – Sistema de Gerenciamento de Vacinação de Pets

📌 Descrição do Projeto
O PetVac é um sistema desenvolvido para auxiliar clínicas veterinárias no gerenciamento de pets, tutores, usuários internos e principalmente controle de vacinas, suas datas de aplicação, próximas doses e histórico.

O sistema possui:
● Backend em Python, utilizando Pandas como “banco de dados” baseado em arquivos
CSV.
● Frontend em Streamlit, permitindo uma interface simples e funcional para
recepcionistas e veterinários.
● Organização modular para facilitar manutenção, leitura e evolução do projeto.

O PetVac foi projetado para uso exclusivo da clínica, onde somente veterinários e recepcionistas têm acesso ao sistema.

→ Tecnologias Utilizadas
● Python: para a lógica do backend.
● Pandas: para manipulação dos dados.
● Streamlit: para a interface visual.
● CSS (customização das telas)
● CSV - Armazenamento dos dados:
○ vacinas.csv
○ pets.csv
○ tutores.csv
○ usuarios.csv
○ notificacoes.csv

→ Como Rodar o Projeto Localmente
1. Clonar o repositório
git clone <repo-url>
cd PetVac_package

2. Criar e ativar o ambiente virtual
Windows
python -m venv .venv
.venv\Scripts\activate

macOS / Linux
python -m venv .venv
source .venv/bin/activate

3. Instalar dependências
pip install -r requirements.txt

4. Executar o Streamlit
python -m streamlit run frontend/app.py
ou
streamlit run frontend/app.py

📂 Estrutura de Pastas
PETVAC/
│
├── backend/
│ ├── database.py # Carregamento e salvamento dos dados
│ ├── historico_vacinas.py # Classe HistóricoVacinas
│ ├── pet.py # Classe e operações de Pets
│ ├── services.py # Funções principais da lógica do sistema
│ ├── tutor.py # Classe e operações de Tutores
│ ├── usuario.py # Classe Usuários
(veterinários/recepcionistas)
│ └── vacina.py # Classe Vacina
│
├── data/
│ ├── vacinas.csv
│ ├── pets.csv
│ ├── tutores.csv
│ ├── usuarios.csv
│
├── frontend/
│ ├── app.py # Arquivo principal Streamlit
│ ├── style.py # CSS das telas
│ └── pages/
│ ├── cadastro_pet.py
│ ├── cadastro_tutor.py
│ ├── historico.py
│ ├── login.py
│ └── vacinas.py
│
└── README.md
