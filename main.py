#FUNCAO SUPERMERCADO
def supermercado():
    carrinho = []
    total = 0

    while True: #MENU MERCADO
        print("\n" + "=" * 30)
        print("      MERCADO")
        print("=" * 30)
        print("1 - Adicionar produto")
        print("2 - Ver carrinho")
        print("3 - Ver total da compra")
        print("4 - Finalizar compra")
        print("0 - Voltar")
        print("=" * 30)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: R$ "))

            carrinho.append((nome, preco))
            total += preco

            print(f"{nome} adicionado ao carrinho!")

        elif opcao == "2":
            if len(carrinho) == 0:
                print("Carrinho vazio!")
            else:
                print("\n=== CARRINHO ===")
                for produto, preco in carrinho:
                    print(f"{produto} - R$ {preco:.2f}")

        elif opcao == "3":
            print(f"Total atual: R$ {total:.2f}")

        elif opcao == "4":
            print("\n=== COMPRA FINALIZADA ===")
            print(f"Valor total: R$ {total:.2f}")
            break

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

#FUNCAO PAR OU IMPAR
def par_ou_impar():
    print("=" * 30)
    print('Seja bem-vindo(a) ao sistema de verificacao de impar ou par!')
    numero = int(input('Digite um numero:'))

    if numero % 2 == 0:
        print('Número é PAR.')
    else:
        print('Número é IMPAR.')

#FUNCAO CALCULAR IMC
def imc():
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))

    imc = peso / (altura ** 2 )

    print(f'IMC: {imc:.2f}')

    if imc < 16:
        print("Seu estado é de Magreza grave.")

    elif imc < 17:
        print("Seu estado é de Magreza moderada.")

    elif imc < 18.5:
        print("Seu estado é de Magreza leve.")

    elif imc < 25:
        print("Você está Saudável.")

    elif imc < 30:
        print("Seu estado é de Sobrepeso.")

    elif imc < 35:
        print("Seu estado é de Obesidade Grau I.")

    elif imc < 40:
        print("Seu estado é de Obesidade Grau II (severa).")

    else:
        print("Seu estado é de Obesidade Grau III (mórbida).")

#MENU PRINCIPAL
while True:

    print("\n=== SISTEMA MULTIFUNCIONAL ===")
    print("1. Sistema SuperMercado")
    print("2. Sistema Par ou Impar")
    print("3. Sistema De IMC")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        supermercado()
    
    elif opcao == 2:
        par_ou_impar()

    elif opcao == 3:
        imc()

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção Invalida!")

