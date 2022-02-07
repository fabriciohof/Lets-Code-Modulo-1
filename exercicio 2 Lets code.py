# Faça um programa que leia a validade das informações:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro;
# O programa deve imprimir uma mensagem de erro para cada informação
# inválida.


idade = int(input('Digite sua idade entre 0 e 150: '))
while idade> 150 or idade<0:
    print('Número invalido,digite novamente sua idade:')
    idade = int(input('Digite novamente sua idade: '))
    
salario = float(input('Digite seu salário: '))
while salario<0:
    print('Seu salário deve ser maior que 0 ')
    salario = float(input('Digite seu salário novamente: '))

sexo = str(input('Digite aqui seu sexo: \n entre M,F ou outro '))
while sexo != str("M") and sexo != str("F") and sexo != str("outro") :
    print('Voce só pode responder M,F ou outro')
    sexo = str(input('Digite aqui seu sexo: '))