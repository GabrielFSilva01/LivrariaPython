from Classes.Cidade import Cidade
from Classes.Pessoa import Pessoas
from Classes.Autor import autores
from Classes.Editora import editoras
from Classes.Genero import generos
from Classes.Livros import livros
from Classes.Emprestimos import emprestimos

# Dicionários (repositórios em memória)
dict_cidades = {
   
   1: Cidade(1, "São Paulo", "SP"),
    2: Cidade(2, "Rio de Janeiro", "RJ"),
    3: Cidade(3, "Belo Horizonte", "MG"),
    4: Cidade(4, "Porto Alegre", "RS"),
    5: Cidade(5, "Curitiba", "PR")

}
dict_pessoas = {
     1001: Pessoas(1001, "Ana Silva", 12345678901, "Rua A, 123", 1), # SP
    1002: Pessoas(1002, "Bruno Costa", 10987654321, "Av. B, 456", 2), # RJ
    1003: Pessoas(1003, "Carla Dias", 11223344556, "Trav. C, 789", 3)  # MG
}
dict_autores = {
     101: autores(101, "Machado de Assis"),
    102: autores(102, "Clarice Lispector"),
    103: autores(103, "Gabriel Garcia Marquez"),
    104: autores(104, "Stephen King"),
    105: autores(105, "J.K. Rowling")
}
dict_editoras = {
    201: editoras(201, "Companhia das Letras", 1), # SP
    202: editoras(202, "Rocco", 2),               # RJ
    203: editoras(203, "Aleph", 1),               # SP
    204: editoras(204, "Arqueiro", 3)             # MG
}
dict_generos = {
    301: generos(301, "Ficção Científica"),
    302: generos(302, "Fantasia"),
    303: generos(303, "Romance"),
    304: generos(304, "Suspense"),
    305: generos(305, "Literatura Clássica")
}
dict_livros = {
    4001: livros(4001, "Dom Casmurro", 201, 101, 305, True),   # Disponível
    4002: livros(4002, "A Hora da Estrela", 201, 102, 305, True), # Disponível
    4003: livros(4003, "Cem Anos de Solidão", 202, 103, 303, False), # Emprestado
    4004: livros(4004, "It - A Coisa", 203, 104, 304, True),    # Disponível
    4005: livros(4005, "Harry Potter", 204, 105, 302, True)     # Disponível
}
dict_emprestimos = {
    5001: emprestimos(5001, 1001, 4003, "2024-06-25", "2024-07-02"), # Livro 4003 emprestado para 1001, não devolvido
    5002: emprestimos(5002, 1002, 4001, "2024-06-20", "2024-06-27") # Empréstimo devolvido com atraso
}


def cadastrar_cidade():
    print("\n--- Cadastro de Cidade ---")
    codigo = int(input("Código da cidade: "))
    descricao = input("Descrição: ")
    uf= (input("Unidade Federal: "))

    if codigo in dict_cidades:
        print("Código já existe. Cidade não cadastrada.")
        return None
    
    cidade = Cidade(codigo, descricao,uf)
    dict_cidades[codigo] = cidade
    print("Cidade cadastrada com sucesso!")
    return cidade


def cadastrar_pessoa():
    print("\n--- Cadastro de Pessoa ---")

    codigo = int(input("Código da pessoa: "))
    nome = input("Nome: ")
    endereco = input("Endereço: ")

    # ** A leitura e validação do CPF ACONTECEM AQUI! **
    cpf_final_validado = "" # Esta variável vai guardar o CPF quando ele for validado
    cpf_valido = False
    while not cpf_valido:
        # AQUI é onde o CPF é lido, e essa é a leitura que será validada
        cpf_input_usuario = input("CPF (11 números, sem pontos ou traços): ") 
        
        if len(cpf_input_usuario) == 11 and cpf_input_usuario.isdigit():
            cpf_final_validado = cpf_input_usuario # Se válido, armazena para uso posterior
            cpf_valido = True
            print("CPF validado com sucesso!!")
        else:
            print(f"Erro: O CPF deve ter exatamente 11 dígitos numéricos. Você digitou '{cpf_input_usuario}' ({len(cpf_input_usuario)} dígitos). Tente novamente.")
    # Ao sair do loop 'while', 'cpf_final_validado' conterá o CPF correto como string.

    # ** Validação do Código da Cidade **
    print("\nCidades disponíveis:")
    if not dict_cidades: # Boa prática: verificar se há cidades cadastradas
        print("Nenhuma cidade cadastrada. Por favor, cadastre cidades primeiro.")
        return None 
        
    for cid in dict_cidades.values():
        print(f"{cid.codigo} - {cid.descricao} ({cid.uf})") 

    codigo_cidade = int(input("Código da Cidade: "))
    cidade_encontrada = dict_cidades.get(codigo_cidade)

    if not cidade_encontrada:
        print("Cidade não encontrada. Pessoa não cadastrada.")
        return None

    # Cria o objeto Pessoas, convertendo 'cpf_final_validado' para inteiro
    pessoa = Pessoas(codigo, nome, int(cpf_final_validado), endereco, codigo_cidade)
    
    # Adiciona a pessoa ao dicionário
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

    # 1. Validação de Duplicidade do Código do Livro
    while True:
        try:
            codigo = int(input("Código do livro: "))
            if codigo in dict_livros:
                print(f"Erro: O código {codigo} já existe. Por favor, digite um código diferente.")
            else:
                break # Sai do loop se o código for válido e não duplicado
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o código.")

    nome = input("Nome do livro: ")

    # 2. Validação da Editora (usando loop para garantir entrada válida)
    while True:
        print("\nEditoras disponíveis:")
        if not dict_editoras:
            print("Nenhuma editora cadastrada. Cadastre uma editora primeiro.")
            return None # Aborta se não houver editoras para escolher

        for editora_obj in dict_editoras.values(): # Use um nome de variável diferente para não confundir com a dataclass
            print(f"{editora_obj.codigo} - {editora_obj.nome}")
        
        try:
            codigo_editora = int(input("Código da Editora: "))
            if codigo_editora in dict_editoras:
                print(f"Editora encontrada: {dict_editoras[codigo_editora].nome}")
                break # Sai do loop se a editora for encontrada
            else:
                print("Código da Editora não encontrado. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # 3. Validação do Autor (usando loop para garantir entrada válida)
    while True:
        print("\nAutores disponíveis:")
        if not dict_autores:
            print("Nenhum autor cadastrado. Cadastre um autor primeiro.")
            return None # Aborta se não houver autores

        for autor_obj in dict_autores.values():
            print(f"{autor_obj.codigo} - {autor_obj.nome}")
        
        try:
            codigo_autor = int(input("Código do Autor: "))
            if codigo_autor in dict_autores:
                print(f"Autor encontrado: {dict_autores[codigo_autor].nome}")
                break
            else:
                print("Código do Autor não encontrado. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # 4. Validação do Gênero (usando loop para garantir entrada válida)
    while True:
        print("\nGêneros disponíveis:")
        if not dict_generos:
            print("Nenhum gênero cadastrado. Cadastre um gênero primeiro.")
            return None # Aborta se não houver gêneros

        for genero_obj in dict_generos.values():
            print(f"{genero_obj.codigo} - {genero_obj.descricao}") # Use descricao, não nome
        
        try:
            codigo_genero = int(input("Código do Gênero: "))
            if codigo_genero in dict_generos:
                print(f"Gênero encontrado: {dict_generos[codigo_genero].descricao}")
                break
            else:
                print("Código do Gênero não encontrado. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # 5. Disponibilidade do Livro (mantida sua lógica, que está ótima!)
    disponivel = input("Disponível (s/n): ").strip().lower() == 's'

    # Criação e armazenamento do objeto livro
    livro = livros(codigo, nome, codigo_editora, codigo_autor, codigo_genero, disponivel)
    dict_livros[codigo] = livro
    print("\nLivro cadastrado com sucesso!")
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
