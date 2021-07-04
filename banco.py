from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('++++++++++++++++++++++++')
    print('__________ATM___________')
    print('++++++++Geek Bank+++++++')
    print('________________________')

    print('Selecione uma opcao no menu')
    print('1 - Criar Conta')
    print('2 - Efetuar Saque')
    print('3 - Efetivar deposito')
    print('4 - Efetuar tranferencia')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte Sempre')
        sleep(2)
        exit(0)
    else:
        print('Opcao Invalida')
        sleep(2)
        menu()



def criar_conta() -> None:
    print('Informe os dados do cliente')

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados da conta')
    print(conta)
    sleep(2)
    menu()



def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Nao foi encontrada a conta com numero {numero}')
    else:
        print('Ainda nao existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('informe o numero da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('informe o valor do deposito: '))

            conta.depositar(valor)
        else:
            print(f'Nao foi encontrada a conta com numero {numero}')
    else:
        print('Ainda nao existem contas cadastradas.')

    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('informe o numero da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('informe o numero da conta destino: '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferencia: '))

                conta_o.transferir(conta_d, valor)

            else:
                print(f'a conta destino numero {numero_d} nao foi encontrada.')
        else:
            print(f'a sua conta com numrero {numero_o} nao foi encontrada')
    else:
        print('Ainda nao existem contas cadastradas.')

    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('______________')
            sleep(1)
    else:
        print('Nao existem contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()



