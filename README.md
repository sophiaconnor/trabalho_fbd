# trabalho_fbd
trabalho da disciplina de fundamentos de banco de dados

Para rodar o projeto, cada membro só precisa abrir o terminal do Codespaces deles e colar o comando do Docker: docker run --name meu_postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=trabalho_fbd -p 5432:5432 -d postgres:16

e carregar o arquivo .sql:
docker exec -i meu_postgres psql -U postgres -d trabalho_fbd < banco.sql
