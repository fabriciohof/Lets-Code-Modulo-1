#Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.

num= (int(input('Digite um número para tabuada: ')))
for count in range(10):
    print("%d x %d = %d" % (num, count+1, num*(count+1)) )