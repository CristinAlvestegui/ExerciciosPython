def Exercicio01():
    A = 10
    B = 20
    msg = "Antes da troca: A= {}, B = {}".format(A,B)
    aux = A
    A = B
    B = aux
    msg = msg + "\nDepois da troca: A= {} , B = {}".format(A,B)
    return msg

def Exercicio02(num1):
    return num1 - 1

def E3(base,altura):
    area = base * altura
    msg = 'A Area do Retângulo é: {}'.format(area)
    return msg

def E4(dia, mes, ano):
    dia = int(dia)
    mes = int(mes * 30)
    ano = int(ano * 365)
    idade = dia + (mes + ano)
    msg = 'Sua idade expressa em dias é: {}'.format(idade)
    return msg

def E5():
    return 'oi'