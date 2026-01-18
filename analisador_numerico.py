def ler_numeros():
    while True:
        try:
            numeros = list(map(int, input('Digite números inteiros separando-os por espaço: ').split()))
            
            return numeros
        except ValueError:
            print('\nDigite apenas números inteiros\n')
            
            
            
def separar_numeros(numeros):
    pares = []
    impares = []
    
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
            
    return pares, impares

def quantidade_pares_impares(pares, impares):
    return len(pares), len(impares)

def menor_maior(lista):
    menor = lista[0]
    maior = lista[0]
    
    for n in lista[1:]:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        
    return menor, maior

def menu():
    print('\n====================MENU====================')
    print('1 - Mostrar números pares')
    print('2 - Mostrar números ímpares')
    print('3 - Mostrar a quantidade de números pares')
    print('4 - Mostrar a quantidade de números ímpares')
    print('5 - Mostrar o menor número par')
    print('6 - Mostrar o maior número par')
    print('7 - Mostrar o menor número ímpar')
    print('8 - Mostrar o maior número ímpar')
    print('0 - Sair')
    
    
def main():
    try:
        numeros = ler_numeros()
        pares, impares = separar_numeros(numeros)
        qtde_pares, qtde_impares = quantidade_pares_impares(pares, impares)
        menor_p, maior_p = (menor_maior(pares) if pares else (None, None))
        menor_i, maior_i = (menor_maior(impares) if impares else (None, None))
        
        while True:
            menu()
            opcao = input("Escolha uma das opções\n")

                
            if opcao == '0':
                print('\nSaindo...')
                break
            
            elif opcao == '1':
                print('----------------')
                print(f'Pares: {pares}' if pares else "Não há números pares")
                print('----------------')
                
            elif opcao == '2':
                print('----------------')
                print(f'Ímpares: {impares}' if impares else 'Não há números ímpares')
                print('----------------')
                
            elif opcao == '3':
                print('----------------')
                print(f'Existem {qtde_pares} pares' if qtde_pares else "Não há números pares")
                print('----------------')
                
            elif opcao == '4':
                print('----------------')
                print(f'Existem {qtde_impares} ímpares' if qtde_impares else "Não há números ímpares")
                print('----------------')
                
            elif opcao == '5':
                if menor_p is not None:
                    print('----------------')
                    print(f'Menor número par é: {menor_p}')
                    print('----------------')
                else:
                    print('----------------')
                    print("Não há números pares")
                    print('----------------')
                    
            elif opcao == '6':
                if maior_p is not None:
                    print('----------------')
                    print(f'Maior número par é: {maior_p}')
                    print('----------------')
                else:
                    print('----------------')
                    print("Não há números pares")
                    print('----------------')
                    
            elif opcao == '7':
                if menor_i is not None:
                    print('----------------')
                    print(f'Menor número ímpar: {menor_i}')
                    print('----------------')
                else:
                    print('----------------')
                    print("Não há números ímpares")
                    print('----------------')
                    
            elif opcao == '8':
                if maior_i is not None:
                    print('----------------')
                    print(f'Maior número ímpar: {maior_i}')
                    print('----------------')
                else:
                    print('----------------')
                    print('Não há números ímpares')
                    print('----------------')
                    
            else:
                print('----------------')
                print("Opção inválida!")
                print('----------------')
                    
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.\n")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == '__main__':
    main()  