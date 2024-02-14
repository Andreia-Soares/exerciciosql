# Sistema de Gerenciamento de Compras

Este é um projeto de aula do Bootcamp Data Analytics WoMakersCode para um sistema de gerenciamento de compras, que inclui a criação de duas tabelas em um banco de dados SQLite: "clientes" e "compras".

## Descrição

O sistema consiste em duas tabelas:

- **clientes**: Armazena informações sobre os clientes, incluindo nome, idade, e saldo.
- **compras**: Registra as compras realizadas pelos clientes, incluindo o produto adquirido e o valor da compra.

## Estrutura do Banco de Dados

### Tabela "clientes"

| Coluna      | Tipo     | Descrição            |
|-------------|----------|----------------------|
| id          | INT      | Chave Primária       |
| nome        | TEXT     | Nome do Cliente      |
| idade       | INT      | Idade do Cliente     |
| saldo       | REAL     | Saldo do Cliente     |

### Tabela "compras"

| Coluna      | Tipo     | Descrição                            |
|-------------|----------|--------------------------------------|
| id          | INT      | Chave Primária                       |
| cliente_id  | INT      | Chave Estrangeira para clientes(id) |
| produto     | TEXT     | Nome do Produto                      |
| valor       | REAL     | Valor da Compra                      |

## Como Utilizar

1. Clone o repositório.
2. Execute o script Python para criar o banco de dados e inserir dados de exemplo.
3. Explore as funcionalidades do sistema.

## Exemplo de Consulta SQL

Para exibir o nome do cliente, o produto e o valor de cada compra, utilize a seguinte consulta SQL:

```sql
SELECT c.nome AS nome_cliente, co.produto, co.valor
FROM compras co
INNER JOIN clientes c ON co.cliente_id = c.id
