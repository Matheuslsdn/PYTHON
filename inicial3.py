# numero = int(input("Digite um número"))

# if numero < 0:
#     print("O número é negativo")

# if numero > 0:
#     print("O número é positivo")

# if numero == 0:
#     print("O número é zero")

# #Prática

# num = int(input("digite um número "))

# if num == 1984:
#     print(f"{num} Orwell")
# print(num) 

#atividade 16

# num1 = int(input("Digite um número "))
# if num1 < 0: 
#     print(f"{num1 * -1}")
# else:
#     print(num1)

#atividade 17

# custo = 5.9
# nome = str(input("Qual o seu nome "))

# if nome == 'jerry':
#     print(custo)
# else:
#     porcao = int(input("Quantas porções foram compradas "))
#     print(f"O valor da total da porção é de: {porcao * custo}")

#atividade 18
# numero1 = int(input("digite um número "))
# if numero1 >= 100 < 1000:
#     print(f"número é menor que 1000, Obrigado!")  
# if numero1 >= 10 < 100:
#     print(f"número é menor que 1000 e menor que 100, Obrigado!")
# if numero1 < 10:
#     print(f"número é menor que 1000, menor que 100 e menor 10, Obrigado!")    
# if numero1 >= 1000:
#     print("Obrigado!") 


#atividade 19
# name = "João"
# cidade = "Curitiba"
# estado = "Paraná"
# cep = 55555123

# user = input("Digite seu nome ") 
# if user == "João" :
#     print(f"Bem vindo {name, cidade, estado, cep}")
# if user != "João":
#     print("Esse usuário não existe em nosso banco de dados")

#atividade 20 
# a = int(input("Digite um número "))
# b = int(input("Digite um número "))
# op = str(input("Escreva um operador "))

# if op == "+":
#     print(f"a soma é {a + b}")
# if op == "-":
#     print(f"a subtração é {a - b}")
# if op == "*":
#     print(f"a multiplicação é {a * b}")
 
#atividade 21
# Fahrenheit = float(input("Digite a temperatura atual em fahrenheit é de "))
# Celsius =  (Fahrenheit - 32) / 1.8

# if Celsius < 0:
#     print("Brrl, está frio aqui")

#atividade 22
# salarioHora = float(input("Quanto você ganha por hora? "))
# horasTrabalhadas = int(input("Quantas horas você trabalhou hoje "))
# diaDaSemana = str(input("Que dia da semana que é "))

# if diaDaSemana == "Domingo" "domingo":
#     print(f"Você recebe hoje:{(salarioHora * horasTrabalhadas) * 2}")
# else:
#     print(f"Você recebe hoje:{salarioHora * horasTrabalhadas}")

#atividade 23 
# card = int(input("quantos pontos o cliente possui? "))
# if card >= 100:
#     print(f"Você tem 15% de BÔNUS, seu saldo atual de bônus é de {card + ((card / 100) * 15)}")
# if card <= 99:
#     print(f"você tem 10% de BÔNUS, seu saldo atual de bônus é de {card + ((card / 100) * 10)}")

#atividade 24
# temperatura = float(input("Qual a temperatura de amanhã? "))
# clima = str(input("Qual é o clima de amanhã? "))
# if temperatura >= 20:
#     print("Está calor vista uma bermuda e uma regata")
# if temperatura <= 19 >= 10:
#     print("Está meio frio vista uma calça e uma blusa")
# if temperatura < 10 >= 5:
#     print("Está muito frio vista muita roupa, calça moleton, blusas e sapatos quentes")
# if clima == "Ensolarao" "ensolarado":
#     print("pode sair tranquilo.")
# else:
#     print("Mas leve um guarda-chuva, pode chover")

#atividade 25
# idade = int(input("Qual a sua idade? "))
# if idade >= 18:
#     print("Você é de maior")
# else:
#     print("Você é de menor")

#atividade 26
# bim1 = float(input("Qual foi a nota do primerio bimestre? "))
# bim2 = float(input("Qual foi a nota do segundo bimestre? "))
# bim3 = float(input("Qual foi a nota do terceiro bimestre? "))
# bim4 = float(input("Qual foi a nota do quarto bimestre? "))
# media = (bim1 + bim2 + bim3 + bim4) / 4
# print(media)
# if media >= 7.0:
#     print("Aprovado!")
# else:
#     print("Reprovado!")

#atividade 27
# A = "Categoria Premium"
# B = "Categoria Intermedária"
# C = "Categoria Eonômica"
# valor = float(input("Qual é o valor do produto? "))

# if valor > 100:
#     print(f"O produto é de {A}")
# else: 
#     if valor >= 51 <=100:
#         print(f"O produto é de {B}")
#     else:
#         print(f"O produto é de {C}")

#atividade 28
# idade1 = int(input("Qual é a sua idade? "))
# if idade1 < 18:
#     print("Você não é obrigado a votar!")
# else:
#     if idade1 <= 65 >= 18:
#         print("Você é obrigado a votar")
#     else:
#         print("Você pode votar, mas não é obrigado!")

#atividade 29
# mes = int(input("Digite o numero do mês requerido: "))

# if mes == 1:
#     print("Janeiro")
# else:
#     if mes == 2:
#         print("Fevereiro")
#     else:
#         if mes == 3:
#             print("Março")
#         else:
#             if mes == 4:
#                 print("Abril")
#             else:
#                 if mes == 5:
#                     print("Maio")
#                 else:
#                     if mes == 6:
#                         print("Junho")
#                     else:
#                         if mes == 7:
#                             print("Julho")
#                         else:
#                             if mes == 8:
#                                 print("Agosto")
#                             else:
#                                 if mes == 9:
#                                     print("Setembro")
#                                 else:
#                                     if mes == 10:
#                                         print("Outubro")
#                                     else:
#                                         if mes == 11:
#                                             print("Novembro")
#                                         else:
#                                             if mes == 12:
#                                                 print("Dezembro")
#                                             else:
#                                                 print("Mês inválido")

#atividade 30
# num10 = int(input("Digite um numero: "))
# num11 = int(input("Digite um numero: "))

# if num10 > num11:
#     print(num10)
# elif num10 < num11:
#     print(num11)
# else:
#     print("Os numeros são iguais")

#atividade 31
# nome1 = str(input("Qual é o seu nome? "))
# idade1 = int(input("Qual é a sua idade? "))
# nome2 = str(input("Qual é o seu nome? "))
# idade2 = int(input("Qual é a sua idade? "))

# if idade1 > idade2:
#     print(f"O {nome1} é mais velho que {nome2} ")
# elif idade1 < idade2:
#     print(f"O {nome2} é mais velho que {nome1} ")
# else:
#     print(f"{nome1} e {nome2} tem a mesma idade")

#atividade 32 - Cola
# numero5 = int(input("Digite um número "))

# if numero5 >= 5 and numero5 <= 8:
#     print("O número está entre 5 e 8")


# numero6 = int(input("Digite um número "))

# if numero6 >= 5 or numero6 <= 8:
#     print("O número está entre 5 e 8")

#atividade 33 
# idade = int(input("Qual é a sua idade? "))

# if idade < 5 and idade > 100:
#     print("Idade inválida")
# elif idade <= 5:
#     print("Se você realmente tivesse essa idade não saberia ler")
# elif idade > 100:
#     print("Se você realmente tivesse essa idade não estaria mexendo nesse aparelho")
# elif idade >= 6 and idade < 15:
#     print("Você é uma criança, vai estudar e larga esse free fire")
# elif idade >= 16 and idade < 58:
#     print("Você é um adulto, vai trabalhar e cuida dessa saúde meu parça")
# else:
#     print("Vou nem dizer nada, você pode morrer a qualquer momento, CUIDADO")

#atividade 34
# nome = str(input("Digite seu nome "))

# if nome == "huguinho" or nome == "zezinho" or nome == "luizinho":
#     print("Você é um sobrinho do pato Donald")
# elif nome == "chiquinho" or nome == "francisquinho":
#     print("Você é um sobrinha do Mickey Mouse")
# else:
#     print("Você não é sobrinho de ninguém")

#atividade 35
# nota = int(input("Qual foi sua ponuação total da prova? "))

# if nota < 0:
#     print("Nota inválida")
# elif nota >= 0 and nota <= 49:
#     print("Você foi reprovado")
# elif nota >= 50 and nota <= 59:
#     print("1")
# elif nota >= 60 and nota <= 69:
#     print("2")
# elif nota >= 70 and nota <= 79:
#     print("3")
# elif nota >= 80 and nota <= 89:
#     print("4")
# elif nota >= 90 and nota <= 100:
#     print("5")
# else:
#     print("impossivel passar de 100")

#atividade 36
# numero = int(input("Digite um número "))

# if numero % 3 == 0:
#     print("fizz")
# elif numero % 5 == 0:
#     print("buzz")
# else:
#     print("fizzbuzz")


#atividade 37
# ano = int(input("Digite o ano você está "))

# if ano % 4 == 0 or ano % 100 != 0 and ano % 400 == 0:
#     print("O ano é bissexto")
# else:
#     print("O ano não é bissexto")

#atividade 38 - laços de repetição While
# while True:
#     numero = int(input("entre com um número: ou diite -1 para parar "))
#     if numero == -1:
#         break
#     print(numero ** 2)

# print("programa encerado, obrigado!")

# while True:
#     codigo = input("Por favor, insira o PIN: ")
#     if codigo == "1234":
#         break
#     print("Errado!... tente de novo")

# print("Pin correto! Obrigado")
# print("Olá")
# while True:
#     texto = str(input("Você deseja continuar? "))
#     if texto == "não":
#         break
#     print(input("Você deseja continuar? "))

# print("Okay, até a próxima!")

#atividade 39
# from math import sqrt
# while True:
#     numero = int(input("Digite um número: "))
#     if numero < 0:
#         print("Número inválido! ")
#     else:
#         print(sqrt(numero))  
#         break

# atividade 40
# numero = 5
# print("Contagem")

# while True:
#     print(numero)
#     numero = numero - 1
#     if numero == 0:
#         break
# print("Fim!")

#atividade 41
# senha1 = int(input("Qual é a Senha? "))
# while True:
#     senha2 = int(input("Senha? "))
#     if senha1 == senha2:
#         print("Acesso permitido! Obrigado")
#         break
#     else:
#         print("Senha inválida! Tente novamente")
        
#atividade 42
# tentativas = 0 
# while True:
#     codigo = input("Por favor, digite seu pin: ")
#     tentativas += 1
#     if codigo == "1234":
#         sucesso = True
#         break
#     if tentativas == 3:
#         sucesso = False
#         break
#     print("Incorreto... tente novamente")
# if sucesso == True:
#     print("Acesso permitido! Obrigado")
# else:
#     print("Acesso negado! Tente novamente mais tarde")

# pin = 1234
# tentativas = 0
# while True:
#     codigo = input("Por favor, digite seu pin: ")
#     tentativas += 1
#     if codigo == str(pin):  # Convert pin to string for comparison
#         print("Acesso permitido! Obrigado")
#         break
#     else:
#         print("Incorreto... tente novamente")
#         print(tentativas)

#atividade 43
# ano = int(input("Em que ano estamos? "))

# if ano % 4 == 0:
#     print("É ano bissexto.")
# else:
#     print("Não é ano bissexto.")

# while True:
#     ano += 1
#     if ano % 4 == 0:
#         print(f"O próximo ano bissexto será em {ano}")
#         break

#atividade 44
# numero = 0
# while True:
#     numero += 1
#     if numero > 30:
#         break
#     if numero % 2 == 0:
#         print(numero)
    
#atividade 45
# print("Você está pronto? ")
# numero = int(input("Por favor, digite um número: ")) 
# while True:
#     numero = numero - 1
#     if numero == 0:
#         break 
#     print(numero)
# print("Agora!")
    
#atividade 46
# numero = int(input("Por favor, digite um número: "))
# soma = 1
# while True:
#     print(soma)
#     soma += 1
#     if soma > numero:
#         break

# print("Pronto")

#atividade 47
# limite = int(input("Digite um número limite: "))
# numero = 1
# while True:
#     print(numero)
#     numero = numero * 2
#     if numero > limite:
#         break

#atividade 48
# limite = int(input("Digite um número limite: "))
# base = 2
# numero = 1
# while numero <= limite:
#     print(numero)
#     numero *= base

#atividade 49
# limite = int(input("Digite um número limite: "))
# numero = 1
# while True:
#     print(numero)
#     numero = numero * 2
#     if numero > limite:
#         break        
        
#atividade 50
# soma = 0
# while soma < 100:
#     numero = int(input("Digite um número: "))
#     soma += numero
#     if soma >= 100:
#         print(soma)
#         break

#atividade 51
# import re

# senha = input("Digite uma senha: ")
# while len(senha):
#     print(re.search("[A-Z]", senha))
#     print(re.search("[a-z]", senha))
#     print(re.search("[0-9]", senha))
#     break 

#atividade 52
# numero1 = int(input("Adivinhe o número: "))
# import random
# tentativas = 0
# numero2 = random.randint(1, 100)
# while numero1 != numero2:
#     tentativas += 1
#     if tentativas == 5:
#         print("Você perdeu")
#         break
#     numero1 = int(input("Adivinhe o número: "))

#atividade 53
# saldo = 257

# while True:
#     saque = int(input("Qual é o valor que você deseja sacar? "))
#     if saque > saldo:
#         print("Valor indisponível")
#     elif saque % 10 == 0:
#         print("Aguarde o seu saque está sendo efetuado")
#         break
#     else:
#         print("Valor indisponível. Por favor, escolha um valor múltiplo de 10.")

#atividade 54
# texto1 = input("Digite uma palavra: ")
# texto2 = input("Digite uma palavra: ")
# while len(texto1) != len(texto2):
#     print("As palavras possuem quantidades diferentes de letras.")
#     texto2 = input("Digite uma palavra: ")

# print("As palavras possuem a mesma quantidade de letras.")

# inicio = "ex"
# fim = "emplo"
# palavra = inicio + fim
# print(palavra)

# palavra1 = "banana "
# print(palavra1 * 3)

# string_entrada = input("Por favor digite uma string ")
# print(string_entrada)
# print("-" * len(string_entrada))

# texto1 = str(input("Digite uma string: "))
# texto2 = str(input("Digite uma string: "))
# if len(texto1) == len(texto2):
#     print("As strings são igualmente longas")
# elif len(texto1) > len(texto2):
#     print(texto1)
# else:
#     print(texto2)

#atividade 55
# texto = str(input("Coloque uma palavra com o numero de caracteres escolhidos "))
# print("#" * len(texto))

#atividade 56
# texto = str(input("Digite uma string: "))
# print(texto)
# print("-" * len(texto))

#atividade 57
# texto = input("digite uma string: ")
# textode20 = texto.rjust(20, "*")
# print(textode20)
    
#atividade 58
# texto = input("digite uma string: ")
# texto2 = ""
# quadro = texto2.rjust(30, "*")
# print(quadro)
# print(texto)
# print(quadro)

# while True:
#     numero = int(input("Por favor, digite um número: "))
#     if numero == -1:
#         break
#     while numero > 0:
#         print(numero)
#         numero -= 1

# def mensagem():
#     print("Minha pika")

# mensagem()

# def sete_irmaos():
#     print("João")
#     print("Matheus")
#     print("Pedro")
#     print("Paulo")
#     print("Felipe")
#     print("Tito")
#     print("Lucas")
    
# sete_irmaos()