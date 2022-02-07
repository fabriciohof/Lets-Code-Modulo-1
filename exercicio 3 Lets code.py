# Vamos fazer um programa para verificar quem é o assassino de um crime.
# Para descobrir o assassino, a polícia faz um pequeno questionário com 5
# perguntas onde a resposta só pode ser sim ou não:
# a. Mora perto da vítima?
# b. Já trabalhou com a vítima?
# c. Telefonou para a vítima?
# d. Esteve no local do crime?
# e. Devia para a vítima?
# Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
# suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
# 2 pontos são apenas suspeitos, necessitando outras investigações. Valores
# iguais ou abaixo de 1 são liberados.

res1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res2 = int(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res3 = int(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res4 = int(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res5 = int(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
soma_respostas = res1 + res2 + res3 + res4 + res5
if (soma_respostas < 2):
 print("Inocente")
elif (soma_respostas == 2):
 print("Suspeita")
elif (3 <= soma_respostas <= 4):
 print("Cúmplice")
elif (soma_respostas == 5):
 print("Assassino")