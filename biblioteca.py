# Sistema de Biblioteca
# fiz esse programa pra controlar os livros da biblioteca da escola
# da pra cadastrar livro, emprestar pra um aluno e depois dar baixa na devolucao

import json
import os

ARQUIVO = "livros.json"


# carrega os livros do arquivo (se ainda nao existir comeca com a lista vazia)
def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# salva tudo no arquivo pra nao perder quando fechar o programa
def salvar(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(livros, f, ensure_ascii=False, indent=2)


def cadastrar(livros):
    titulo = input("Titulo: ").strip()
    autor = input("Autor: ").strip()
    if titulo == "":
        print("Precisa digitar o titulo")
        return
    livros.append({"titulo": titulo, "autor": autor, "com_aluno": None})
    print("Livro cadastrado!")


def listar(livros):
    if len(livros) == 0:
        print("Nenhum livro cadastrado ainda")
        return
    for i, livro in enumerate(livros, start=1):
        if livro["com_aluno"]:
            situacao = "emprestado para " + livro["com_aluno"]
        else:
            situacao = "disponivel"
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({situacao})")


# mostra a lista e pede o numero do livro
# usei try/except pra nao travar se a pessoa digitar letra ou numero errado
def escolher_livro(livros):
    listar(livros)
    try:
        numero = int(input("Numero do livro: "))
        return livros[numero - 1]
    except (ValueError, IndexError):
        print("Numero invalido")
        return None


def emprestar(livros):
    livro = escolher_livro(livros)
    if livro is None:
        return
    if livro["com_aluno"]:
        print("Esse livro ja esta emprestado")
        return
    livro["com_aluno"] = input("Nome do aluno: ").strip()
    print("Emprestimo feito!")


def devolver(livros):
    livro = escolher_livro(livros)
    if livro is None:
        return
    if not livro["com_aluno"]:
        print("Esse livro nao esta emprestado")
        return
    print(livro["com_aluno"] + " devolveu o livro")
    livro["com_aluno"] = None


def main():
    livros = carregar()
    while True:
        print("\n--- BIBLIOTECA ---")
        print("1 - Cadastrar livro")
        print("2 - Ver livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar(livros)
        elif opcao == "2":
            listar(livros)
        elif opcao == "3":
            emprestar(livros)
        elif opcao == "4":
            devolver(livros)
        elif opcao == "0":
            salvar(livros)
            print("Salvo! Ate mais")
            break
        else:
            print("Opcao invalida")


main()
