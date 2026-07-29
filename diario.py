"""
Diario em Python
"""

import time
import json
import sys


def horario():
    agora = time.strftime("%d/%m/%Y %H:%M:%S")
    return agora


def lerpagina(numero):
    paginas = carregar_paginas()
    print("\n")
    print(paginas[numero - 1]["data"],"\n")
    print(paginas[numero - 1]["nome"],"\n")
    print(paginas[numero - 1]["texto"],"\n")

def carregar_paginas():
    try:
        with open("arquivos.json", "r",encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def salvar_paginas(pagina):
    with open("arquivos.json", "w",encoding="utf-8") as arquivo:
        json.dump(pagina , arquivo,ensure_ascii=False,indent=4)
def editar_pagina():
    paginas = carregar_paginas()
    if not paginas:
        print("\nVocê não tem paginas salvas")
    print("\nSuas páginas do diario:\n")
    for pagina in paginas:
        print(f"Página {pagina["pagina"]}: {pagina["nome"]}")
    while True:
        try: 
            numerodapagina = int(input("\nDigite a página que deseja editar "))
        except ValueError:
            print("\nVocê deve digitar o numero exato da página")
            continue

        for pagina in paginas:
            if pagina["pagina"] == numerodapagina:
                print("\nPagina encontrada!\n")
                print(f"pagina {pagina["pagina"]}")
                print(f"data {pagina["data"]}")
                print(f"titulo: {pagina["nome"]}")
                print(pagina["texto"],"\n")

                while True:
                    print("\nDeseja alterar essa página?")
                    print("1 - sim")
                    alterar = input("2 - não")
                    if alterar in ("1","sim","s"):
                        novo_texto = input("\nDigite o novo texto: ")
                        novo_nome = input("\nQual será o novo titulo? ")
                
                        pagina["nome"] = novo_nome
                        pagina["texto"] = novo_texto
                        pagina["data"] = horario()
                        salvar_paginas(paginas)
                        print("\nPágina atualizada com sucesso!")
                        menu()
                    elif alterar in ("2","não","nao","n"):
                        return
                    else:
                        print("\nOpção invalida!")
                        continue
                




        print("\nPagina não encontrada")
        menu()
            
           


def mostrar_paginas():
    paginas = carregar_paginas()
    if not paginas:
        print("\nVocê não tem paginas salvas")
        return
    print("\nSuas páginas do diario:\n")
    for pagina in paginas:
        print(f"Página {pagina["pagina"]}: {pagina["nome"]}, data: {pagina["data"]}")
    while True:
        try:
            escolha = int(input("\nDigite o numero da pagina que deseja ver: "))
        except ValueError:
            print("\nDigite o numero correto!")
            continue
        encontrou = False
        for pagina in paginas:
            if pagina["pagina"] == escolha:
                print("\nPagina encontrada!\n")
                print(f"pagina {pagina["pagina"]}")
                print(f"data {pagina["data"]}")
                print(f"titulo: {pagina["nome"]}\n")
                print(pagina["texto"],"\n")
                encontrou = True
                break
        if encontrou == False:
            print("\nPagina não encontrada!")
            break
        else:
            break
    while True:    
        print("\n1 - voltar para o menu")
        escolher = input("2 - escolher outra pagina: ").strip().lower()
        if escolher in ("1","voltar para o menu"):
            return
        elif escolher in ("2","escolher outra pagina"):
            mostrar_paginas()
        else:
            print("\nOpção invalida")
            continue
def excluir_paginas():
    paginas = carregar_paginas()
    while True:
        print("para sair digite 0")
        try:
            numero = int(input("\n Digite o numero da pagina que deseja deletar "))
        except ValueError:
            print("\nDigite o numero correto!")
            continue
        encontrou = False
        if numero == 0:
            return
        encontrou = False
        for pagina in paginas:

            if pagina["pagina"] == numero:
                encontrou = True
                paginas.remove(pagina)
                salvar_paginas(paginas)
                print("\nPágina excluida!")
                return
        if encontrou == False:
            print("\nNão encontrei sua pagina")
            return

def criar_nova_pagina():
    print("\nVamos criar sua nova página do diario")
    texto = input("\nDigite o que gostaria de guardar em seu diario: ")
    while True:
        salvar = input("\nDeseja salvar este texto?(s/n): ").lower()
        if salvar in ("s","sim"):
            nome = input("\nQual será o nome(título) da página?: ")
            todas_as_paginas = carregar_paginas()
            if todas_as_paginas:
                numero_da_pagina = max(folha["pagina"] for folha in todas_as_paginas) + 1
            else:
                numero_da_pagina = 1
            
            
            pagina = {

                "nome": nome,
                "texto": texto,
                "data" : horario(),
                "pagina" : numero_da_pagina
                }
            
            todas_as_paginas.append(pagina)
            salvar_paginas(todas_as_paginas)
            return
        elif salvar in ("não","nao","n"):
            return
        else:
            print("\nDesculpe, não entendi sua escolha")
            return
def menu():
    print("\n === Bem vindo ao Diario===")
    while True:
        print("\nSelecione a opção que deseja prosseguir:\n")
        print("1 - ver páginas salvas")
        print("2 - editar páginas")
        print("3 - excluir páginas")
        print("4 - criar nova página")
        print("5 - sair")
        escolha = input("\nEscolha: ").strip().lower()
        if escolha in ("1","ver paginas","ver páginas","ver páginas salvas"):
            mostrar_paginas()
        elif escolha in ("2","editar páginas","editar","editar paginas"):
            editar_pagina()
        elif escolha in ("3","excluir páginas","excluir","excluir paginas"):
            excluir_paginas()
        elif escolha in ("4", "criar nova página"):
            criar_nova_pagina()
        elif escolha in ("5","sair"):
            print("\nEncerrando...")
            time.sleep(2)
            sys.exit()
        else:
            print("\n você selecionou uma opção invalida!")
            continue





if __name__ == "__main__":
    menu()