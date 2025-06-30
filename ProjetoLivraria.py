from dataclasses import dataclass

class Cidade:
    codigo: int
    descricao: str
    
    
class Pessoas:
    codigo: int
    nome: str
    CPF: int
    endereco: str
    codigo_cidade: int

class editoras:
    codigo: int
    nome: str
    codigo_cidade: int
    
class autores:
    codigo: int
    nome: str
    
class generos:
    codigo: int
    descricao: str

class livros:
    codigo:int
    nome: str
    codigo_editora: int
    codigo_autor: int
    codigo_genero: int
    disponivel: bool
    
class emprestimos:
    codigo: int
    codigo_livro: int
    codigo_pessoa: int
    data_empréstimo: str
    data_devolucao: str
    devolvido: bool
    