Visão geral
    O PetVac é um sistema desenvolvido para auxiliar clínicas veterinárias no gerenciamento de pets, tutores, usuários internos e principalmente controle de vacinas.
    
    O projeto foi desenvolvido com Python, Streamlit para o front-end e Pandas para a gestão de dados, com CSV para armazenar os dados.

Backend 

    Classes 
        
        ● tutor.py

            classe Tutor
                atributos    /   utilidade

                idTutor      /   identificar tutor único
                nome         /   nome do tutor
                email        /   email do tutor
                telefone     /   telefone para contato
                endereço     /   endereço do tutor


        ● pet.py

            classe Pet
                atributos      /   utilidade

                idPet          /   identificar pet único
                nome           /   nome do pet
                especie        /   especie do pet
                raca           /   raça do pet
                dataNascimento /   idade do pet
                idTutor        /   conectar pet ao tutor


        ● vacinas.py

            classe Vacina
                atributos       /   utilidade

                idVacina        /   identificar vacina
                idPet           /   conectar vacina ao pet
                nome            /   nome da vacina
                dataAplicacao   /   dia que a vacina foi aplicada
                dataProximaDose /   dia da dose seguinde, se tiver
                status          /   identificar se dose foi aplicada ou está pendente


        ● historico_vacinas.py

            classe HistoricoVacinas
                atributos    /   utilidade

                idHistorico  /   identificar histórico
                idPet        /   conectar historico de vacinas ao pet


        ● usuario.py 

            classe Usuario
                atributos    /   utilidade

                idUsuario    /   identificar usuário
                nome         /   nome do usuário
                senha        /   senha do usuário
                cargo        /   cargo do usuário (recepcionista ou veterinario)


        ● notificacao.py

            classe Notificacao
                Não utilizado por problemas de logistica.


        Relação entre classes:
          Tutor - Pet: um tutor pode ter vários pets. (1-N)
          Pet - Vacina: um pet pode ter varias vacinas. (1-N)
          Pet - HistoricoVacinas: um pet pode ter um historico de vacinas. (1-1)


    Banco de dados

        ● database.py
          Os dados são armazenados em arquivos CSV e são manipulados com a biblioteca Pandas.
  
Fluxo do sistema
    Cadastro:
        Recepcionista cadastra o tutor;
        Recepcionista cadastra o pet e associa ao tutor;
        Dados são salvos no banco de dados.

    Registro de vacinas:
        O recepcionista ou o veterinario associam uma vanica a um pet;
        A vacina entra pro historico de vacinação do pet;
        Dados são salvos no banco de dados.

    Consultar histórico de vacinas:
        O usuário escolhe o pet para verificar o histórico de vacinas;
        O sistema procura o historico do pet;
        O histórico do pet escolhido aparece.




Frontend 
    O frontend foi realizado com a biblioteca streamlit.
