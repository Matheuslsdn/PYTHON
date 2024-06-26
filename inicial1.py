#atividade 06 

numero = int(input("digite um número"))
print(f"{numero}, vezes 5 é:",numero * 5)

#atividade 07

nome = str(input("Qual é o eu nome?"))
ano = int(input("Em que ano você nasceu?"))

print(f"Olá {nome}, você terá {2024 - ano} anos no final do ano de 2024")

#atividade 08

produto = int(input("Qual é o valor do produto?"))
desconto = int(input("Qual é o valor do desconto?"))

print(f"O novo valor do produto é: {produto -  ((produto / 100)* desconto)}")

#atividade 09

valorConta = float(input("Qual o valor da sua conta? "))
percentual = int(input("Qual é a porcentagem da gorjeta?" ))
print(f"O valor da gorjeta é de ", {percentual * (valorConta / 100)})
print(f"O valor total da conta será de {(percentual * (valorConta / 100)) + valorConta}")

#atividade 10

taxa = 0.30
dolar = 5.51
dinheiro = float(input("Qual é o valor que você deseja converter? "))

print(f"O valor convertido com a taxa será de {(dinheiro / dolar) - taxa}")