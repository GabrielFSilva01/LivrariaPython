from funcoes.funcoes import (
    cadastrar_pessoa,
    cadastrar_cidade,
    cadastrar_autor,
    cadastrar_editora,
    cadastrar_genero,
    cadastrar_livro,
    cadastrar_emprestimo
)

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar Cidade")
        print("2 - Cadastrar Pessoa")
        print("3 - Cadastrar Autor")
        print("4 - Cadastrar Editora")
        print("5 - Cadastrar Gênero")
        print("6 - Cadastrar Livro")
        print("7 - Cadastrar Empréstimo")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cidade()
        elif opcao == '2':
            cadastrar_pessoa()
        elif opcao == '3':
            cadastrar_autor()
        elif opcao == '4':
            cadastrar_editora()
        elif opcao == '5':
            cadastrar_genero()
        elif opcao == '6':
            cadastrar_livro()
        elif opcao == '7':
            cadastrar_emprestimo()
        elif opcao == '0':
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
   
    menu_principal() 

   