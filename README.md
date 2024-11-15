<h1 align=center>School API 🏥</br></br><div align=center><img src="http://ForTheBadge.com/images/badges/made-with-python.svg"></div></h1>
<p text-align=justify>Uma API para cadastro de professores, alunos e turmas utilizando Flask e o ORM sqlite. Funcionalidades:</p>

<ul>
  <li>Cadastro de alunos</li>
  <li>Cadastro de professores</li>
  <li>Cadastro de turmas</li>
  <li>Listagem de alunos</li>
  <li>Listagem de professores</li>
  <li>Listagem de turmas</li>
</ul>

<p align=justify>Foi utilizado o SQLITE para criação das tabelas: </p>

```markdown

### Tabela: `TEACHERS`

| Campo         | Tipo         | Descrição                          |
|---------------|--------------|------------------------------------|
| ID            | INTEGER      | PRIMARY KEY                        |
| NOME          | VARCHAR(120) | Nome do professor                  |
| IDADE         | INTEGER      | Idade do professor                 |
| MATERIA       | VARCHAR(120) | Matéria lecionada                  |
| OBSERVACOES   | VARCHAR(120) | Observações sobre o professor      |

### Tabela: `STUDENTS`

| Campo         | Tipo         | Descrição                          |
|---------------|--------------|------------------------------------|
| ID            | INTEGER      | PRIMARY KEY                        |
| NOME          | VARCHAR(120) | Nome do aluno                      |
| IDADE         | INTEGER      | Idade do aluno                     |
| TURMA_ID      | INTEGER      | FOREIGN KEY                        |
| DATA DE NASCIMENTO     | VARCHAR(120) | Data de nascimento        |
| NOTA_PRIMEIRO_SEMESTRE | VARCHAR(120) | Nota do primeiro semestre |
| NOTA_SEGUNDO_SEMESTRE  | VARCHAR(120) | Nota do segundo semestre  |
| MEDIA_FINAL   | FLOAT        | Média final do aluno               |

### Tabela: `CLASSES`

| Campo         | Tipo         | Descrição                          |
|---------------|--------------|------------------------------------|
| ID            | INTEGER      | PRIMARY KEY                        |
| DESCRICAO     | VARCHAR(120) | Descrição da turma                 |
| PROFESSOR_ID  | INTEGER      | FOREIGN KEY                        |
| ATIVO         | VARCHAR(15)  | Status da turma                    |

```

<p align=justify>Para o mapeamento das tabelas foi utilizado o ORM SQLAlchemy</p>
