from Classes.Cidade import Cidade
from Classes.Pessoa import Pessoas
from Classes.Autor import autores
from Classes.Editora import editoras
from Classes.Genero import generos
from Classes.Livros import livros
from Classes.Emprestimos import emprestimos

# Dicionários (repositórios em memória)
dict_cidades = {}
dict_pessoas = {}
dict_autores = {}
dict_editoras = {}
dict_generos = {}
dict_livros = {}
dict_emprestimos = {}


def cadastrar_cidade():
    print("\n--- Cadastro de Cidade ---")
    codigo = int(input("Código da cidade: "))
    descricao = input("Descrição: ")

    if codigo in dict_cidades:
        print("Código já existe. Cidade não cadastrada.")
        return None

    cidade = Cidade(codigo, descricao)
    dict_cidades[codigo] = cidade
    print("Cidade cadastrada com sucesso!")
    return cidade


def cadastrar_pessoa():
    print("\n--- Cadastro de Pessoa ---")
    codigo = int(input("Código da pessoa: "))
    nome = input("Nome: ")
    cpf = int(input("CPF: "))
    endereco = input("Endereço: ")

    print("Cidades disponíveis:")
    for cid in dict_cidades.values():
        print(f"{cid.codigo} - {cid.descricao}")

    codigo_cidade = int(input("Código da Cidade: "))
    cidade = dict_cidades.get(codigo_cidade)

    if not cidade:
        print("Cidade não encontrada. Pessoa não cadastrada.")
        return None

    pessoa = Pessoas(codigo, nome, cpf, endereco, codigo_cidade)
    dict_pessoas[codigo] = pessoa
    print("Pessoa cadastrada com sucesso!")
    return pessoa


def cadastrar_autor():
    print("\n--- Cadastro de Autor ---")
    codigo = int(input("Código do autor: "))
    nome = input("Nome: ")

    if codigo in dict_autores:
        print("Código já existe. Autor não cadastrado.")
        return None

    autor = autores(codigo, nome)
    dict_autores[codigo] = autor
    print("Autor cadastrado com sucesso!")
    return autor


def cadastrar_editora():
    print("\n--- Cadastro de Editora ---")
    codigo = int(input("Código da editora: "))
    nome = input("Nome: ")

    print("Cidades disponíveis:")
    for cid in dict_cidades.values():
        print(f"{cid.codigo} - {cid.descricao}")

    codigo_cidade = int(input("Código da Cidade: "))
    cidade = dict_cidades.get(codigo_cidade)

    if not cidade:
        print("Cidade não encontrada. Editora não cadastrada.")
        return None

    editora = editoras(codigo, nome, codigo_cidade)
    dict_editoras[codigo] = editora
    print("Editora cadastrada com sucesso!")
    return editora


def cadastrar_genero():
    print("\n--- Cadastro de Gênero ---")
    codigo = int(input("Código do gênero: "))
    nome = input("Nome: ")

    if codigo in dict_generos:
        print("Código já existe. Gênero não cadastrado.")
        return None

    genero = generos (codigo, nome)
    dict_generos[codigo] = genero
    print("Gênero cadastrado com sucesso!")
    return genero


def cadastrar_livro():
    print("\n--- Cadastro de Livro ---")
    codigo = int(input("Código do livro: "))
    nome = input("Nome: ")

    print("Editoras disponíveis:")
    for editora in dict_editoras.values():
        print(f"{editora.codigo} - {editora.nome}")
    codigo_editora = int(input("Código da Editora: "))
    if codigo_editora not in dict_editoras:
        print("Editora não encontrada. Livro não cadastrado.")
        return None

    print("Autores disponíveis:")
    for autor in dict_autores.values():
        print(f"{autor.codigo} - {autor.nome}")
    codigo_autor = int(input("Código do Autor: "))
    if codigo_autor not in dict_autores:
        print("Autor não encontrado. Livro não cadastrado.")
        return None

    print("Gêneros disponíveis:")
    for genero in dict_generos.values():
        print(f"{genero.codigo} - {genero.nome}")
    codigo_genero = int(input("Código do Gênero: "))
    if codigo_genero not in dict_generos:
        print("Gênero não encontrado. Livro não cadastrado.")
        return None

    disponivel = input("Disponível (s/n): ").strip().lower() == 's'

    livro = livros(codigo, nome, codigo_editora, codigo_autor, codigo_genero, disponivel)
    dict_livros[codigo] = livro
    print("Livro cadastrado com sucesso!")
    return livro


def cadastrar_emprestimo():
    print("\n--- Cadastro de Empréstimo ---")
    codigo = int(input("Código do empréstimo: "))

    print("Livros disponíveis:")
    for livro in dict_livros.values():
        print(f"{livro.codigo} - {livro.nome} ({'Disponível' if livro.disponivel else 'Indisponível'})")
    codigo_livro = int(input("Código do Livro: "))
    livro = dict_livros.get(codigo_livro)
    if not livro or not livro.disponivel:
        print("Livro não disponível. Empréstimo não realizado.")
        return None

    print("Pessoas disponíveis:")
    for pessoa in dict_pessoas.values():
        print(f"{pessoa.codigo} - {pessoa.nome}")
    codigo_pessoa = int(input("Código da Pessoa: "))
    if codigo_pessoa not in dict_pessoas:
        print("Pessoa não encontrada. Empréstimo não realizado.")
        return None

    data_emprestimo = input("Data de Empréstimo (dd/mm/yyyy): ")
    data_devolucao = input("Data de Devolução (dd/mm/yyyy): ")

    emprestimo = emprestimos(codigo, codigo_livro, codigo_pessoa, data_emprestimo, data_devolucao)
    dict_emprestimos[codigo] = emprestimo
    livro.disponivel = False  # Marcar livro como emprestado
    print("Empréstimo realizado com sucesso!")
    return emprestimo
