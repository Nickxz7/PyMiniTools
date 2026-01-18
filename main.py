from analisador_numerico import main as analisador_numerico
from organizador_lista import main as organizador_lista
from contar_vogais import main as contar_vogais
from pingpong import main as pingpong

def menu():
    print('\n====================MENU====================')
    print('1 - Se deseja entrar no Analisador Numérico')
    print('2 - Se deseja entrar no Organizador de Listas')
    print('3 - Se deseja entrar no Contador de Vogais')
    print('4 - Se deseja entrar no PingPong')
    print('5 - Sair')

def main():
    try:
        while True:
            menu()
            opcao = input('Digite uma das opções: ')
            if opcao == '5':
                print('\nSaindo do programa')
                break
            
            elif opcao == '1':
                analisador_numerico()
            
            elif opcao == '2':
                organizador_lista()

            elif opcao == '3':
                contar_vogais()
            
            elif opcao == '4':
                pingpong()
            
            else:
                print('\nOpção inválida\n')
        
    except Exception as e:
        print(f'Erro inesperado: {e}')

if __name__ == '__main__':
    main()
