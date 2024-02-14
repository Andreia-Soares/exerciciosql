import sqlite3

resoluçãoSQL = sqlite3.connect('exerciciosql')
cursor = resoluçãoSQL.cursor()

# 1- CRIANDO TABELA ALUNOS
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT(100), curso VARCHAR(100));')

# 2- INSERINDO REGISTROS NA TABELA
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Andreia","38","Administracao")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Noemi","24","Pedagogia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Patricia","50","Moda")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Ralf","28","Medicina")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Lucas","19","Engenharia")')

# 3- CONSULTAS BASICAS
# a) SELECIONANDO TODOS OS REGISTROS
#cursor.execute('SELECT * FROM alunos')

# b) SELECIONANDO NOME E IDADE DOS ALUNOS COM MAIS DE 20 ANOS
#dados = cursor.execute('SELECT * FROM alunos WHERE idade>20')

# c) SELECIONANDO OS ALUNOS DE ENGENHARIA EM ORDEM ALFABETICA
#dados = cursor.execute("SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")

# d) CONTANDO O NUMERO TOTAL DE ALUNOS NA TABELA
#dados = cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos')

# 4- ATUALIZAÇÃO E REMOÇÃO
# a) ATUALIZANDO A IDADE DE UM ALUNO ESPECÍFICO NA TABELA
#dados = cursor.execute('UPDATE alunos SET idade="27" WHERE nome="Andreia"')

# b) REMOVENDO UM ALUNO PELO SEU ID
#cursor.execute('DELETE FROM alunos where id=3')

# 5- CRIANDO UMA TABELA E INSERINDO DADOS
#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT(100), saldo FLOAT)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Ivete","38","500")')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2,"Anitta","43","3000")')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3,"Maria","57","7500")')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4,"José","21","10000")')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5,"Pedro","20","23000")')


# 6- CONSULTAS E FUNÇÕES AGREGADAS
# a) SELECIONANDO NOME E IDADE DOS CLIENTES COM IDADE > 30 ANOS
#dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')

# b) CALCULANDO SALDO MEDIO DOS CLIENTES
#cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')

# c) ENCONTRANDO O CLIENTE COM O SALDO MÁXIMO
#cursor.execute('SELECT MAX(saldo) AS saldo_maximo FROM clientes')

# d) CONTANDO QUANTOS CLIENTES TEM SALDO ACIMA DE 1000
#cursor.execute('SELECT COUNT(*) AS total_clientes FROM clientes WHERE saldo >1000')

# 7- ATUALIZAÇÃO E REMOÇÃO COM CONDIÇÕES
# a) ATUALIZANDO O SALDO DE UM CLIENTE ESPECÍFICO
#dados = cursor.execute('UPDATE clientes SET saldo="6300" WHERE nome="Maria"')

# b) REMOVENDO UM CLIENTE PELO SEU ID
#cursor.execute('DELETE FROM clientes where id=1')

# 8- JUNÇÃO DE TABELAS
# CRIANDO UMA SEGUNDA TABELA CHAMADA "COMPRAS", INSERINDO COMPRAS ASSOCIADAS A CLIENTAS DA TABELA "CLIENTES" E EXIBINDO CONSULTA COM NOME DO CLIENTE, PRODUTO E VALOR DA COMPRA

# Criando a tabela "compras"
#cursor.execute('''CREATE TABLE compras ( id INT PRIMARY KEY, cliente_id INT, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))''')
# Inserindo algumas compras associadas a clientes existentes
#cursor.execute("INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, 'Produto A', 50.0)")
#cursor.execute("INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 2, 'Produto B', 100.0)")
#cursor.execute("INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 3, 'Produto C', 150.0)")

# Executando uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
cursor.execute('''SELECT c.nome AS nome_cliente, co.produto, co.valor FROM compras co INNER JOIN clientes c ON co.cliente_id = c.id''')
dados = cursor.fetchall()
for linha in dados:
    print("Cliente:", linha[0])
    print("Produto:", linha[1])
    print("Valor:", linha[2])
    print()


dados = cursor
for alunos in dados:
    print(alunos)

resoluçãoSQL.commit()
resoluçãoSQL.close()
