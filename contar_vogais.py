def contar_vogais(frase):
    i = 0
    vogais = ('aeiou')

    for letra in frase:
        if letra in vogais:
            i += 1

    return i 

    
def main():
    try:
        while True:
            opcao = input(
                'Escolha se deseja contar vogais ou sair\n'
                '(iniciar/sair): '
            ).lower()

            if opcao == 'sair':
                print('\nSaindo do contador de vogais...')
                break

            elif opcao == 'iniciar':
                frase = input('Digite sua frase: ').lower()
                if frase.strip() and not frase.replace("", " ").isdigit():
                    contar = contar_vogais(frase)
                    print(f'\nVogais encontradas: {contar}\n')
                else:
                    print('\nNão digite somente valores numéricos\n')

            else:
                print('\nOpção inexistente, digite novamente\n')

    except Exception as e:
        print(f'Erro inesperado: {e}')


if __name__ == '__main__':
    main()
        
            
                



            