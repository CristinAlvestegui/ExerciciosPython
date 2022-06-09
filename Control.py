import this
import ExerciciosModel
this.opcao = -1


def Menu():
    print('Menu\n\n' +
          '\n1. Exercicio 01' +
          '\n2. Ecercicio 02' +
          '\n3. Exercicio 03' +
          '\n4. Exercicio 04' +
          '\n5. Exercicio 05' +
          '\n0. Sair' +
          '\nEscolha uma das opções acima')
    this.opcao = int(input())

def Pega1():
    print('Informe o primeiro número')
    this.num1 = input()

def PegaD():
    print('Informe os dias que já foram:')
    this.dia = int(input())

def PegaM():
    print('Informe o Mês do seu aniversario:')
    this.mes = int(input())

def PegaA():
    print('Informe sua idade em anos: ')
    this.ano = int(input())

def PegaBase():
    print('Informe a Base do Retângulo')
    this.base = float(input())

def PegaAlura():
    print('Informe a Altura do Retângulo')
    this.altura = float(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado')
        elif this.opcao == 1:
            print(ExerciciosModel.Exercicio01())
        elif this.opcao == 2:
            Pega1()
            print('O antecessor do número: {} é: {}'.format(this.num1, ExerciciosModel.Exercicio02(this.num1)))
        elif this.opcao == 3:
            PegaBase()
            PegaAlura()
            print(ExerciciosModel.E3(this.base, this.altura))

        elif this.opcao == 4:
            PegaD()
            PegaM()
            PegaA()
            print(ExerciciosModel.E4(this.dia, this.mes, this.ano))







