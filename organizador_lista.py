import os
import unicodedata


def sem_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    resultado = ""

    for letra in texto_normalizado:
        if unicodedata.category(letra) != 'Mn':
            resultado += letra

    return resultado

def ler_arquivos(nome_arquivo):
    lista = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    itens = [item.strip() for item in linha.split(',')]
                    lista.extend(itens)
    except FileNotFoundError:
        print("\nArquivo não encontrado\n")
        return []

    return lista

def ordenar(lista):
    if not lista:
        print("\nLista vazia, nenhum conteúdo para ordenar\n")
        return
    
    lista.sort(key=lambda x: sem_acentos(x).lower())
    
    nome_saida = 'resultado_ordenado.txt'
    with open(nome_saida, 'w', encoding='utf-8') as arquivo:
        for item in lista:
            arquivo.write(item + '\n')
    
    print(f'\nArquivo {nome_saida} criado com sucesso!\n')
        

def main():
    try:
        while True:
            opcao = input(
                'Escolha se deseja digitar manualmente, ler um arquivo TXT ou sair?\n'
                'Escreva (digitar/arquivo/sair): '
            ).lower()

            if opcao == 'sair':
                print('\nPrograma encerrado.')
                break

            elif opcao == 'digitar':
                texto = input('Digite sua lista:\n')
                
                if ',' in texto:
                    lista = [item.strip() for item in texto.split(',')]
                else:
                    lista = texto.split()
                
                ordenar(lista)

            elif opcao == 'arquivo':
                nome_arquivo = input('Digite o nome do arquivo da seguinte forma (exemplo.txt): ')
                if os.path.exists(nome_arquivo):
                    lista = ler_arquivos(nome_arquivo)
                    ordenar(lista)
                else:
                    print('\nArquivo inexistente ou nome digitado incorretamente.\n')

            else:
                print('\nOpção inválida\n')
    
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

if __name__ == '__main__':
    main()
    
