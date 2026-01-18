def PingPong(numero):
    i = 1

    while i <= numero:

        if i % 3 == 0 and i % 5 == 0:
            print("PingPong")
        elif i % 3 == 0:
            print("Ping")
        elif i % 5 == 0:
            print("Pong")
        else:
            print(i)

        i += 1

def main():
    try:
        while True:
            opcao = input(
                'Iniciar ping pong ou sair?\n'
                'Digite (iniciar/sair): '
            ).lower()

            if opcao == 'sair':
                print('\nSaindo do ping pong...')
                break

            elif opcao == 'iniciar':
                digito = input("Digite um numero: ").strip()
                if digito.isdigit():
                    numero = int(digito)
                    PingPong(numero)
                else:
                    print('\nDigite apenas números\n')

            else:
                print('\nOpção inválida\n')

    except Exception as e:
        print(f'Erro inesperado: {e}')

if __name__ == '__main__':
    main()
            

