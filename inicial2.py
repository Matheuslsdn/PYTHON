#atividade 11

capital = float(input("Qual o valor inicial? "))
juros = float(input("Qual a taxa de juros anual? "))
tempo = int(input("Quantos anos? "))

print(f"o montante final será de {capital + (capital * (juros / 100) * tempo)}")

#atividade 12

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

print(f"A média dos números é {(num1 + num2 + num3) / 3}")

#atividade 13

largura = float(input("Qual é a largura? "))
altura = float(input("Qual é a altura? "))

print(f"A área é de {largura * altura} e o perimetro é de {2 * (largura + altura)}")

#atividade 14

C = float(input("Qual é a temperatura atual? "))

print(f"Convertido em fahrenheit { C * 9/5 + 32}")

#atividade 15

#3
print("Trocando um pneu furado")
print("1° verifique se o local é seguro")
print("2° sinalize o local")
print("3° verifique os equipamentos")
print("4° erguer o carro")
print("5° remover os parafusos")
print("6° remover o pneu")
print("7° colocar o step")
print("8° colocar os parafusos")
print("9° apertar os parafusos")
print("10° abaixar o carro")
print("11° guardar os equipamentos")
print("12° remover sinalização")
print("pneu trocado")

#4
nota1 = float(input("Qual a nota do 1° bimestre?"))
nota2 = float(input("Qual a nota do 2° bimestre?"))
nota3 = float(input("Qual a nota do 3° bimestre?"))
nota4 = float(input("Qual a nota do 4° bimestre?"))

print(f"A média do aluno é {(nota1 + nota2 + nota3 + nota4) / 4}")
#5
numero = int(input("Digite um numero: "))

if numero % 2 == 0:
     print("O numero é par")
else:
     print("O numero é impar")

#11
local = str(input("Para onde você quer viajar?"))
orcamento = float(input("Qual é o valor que você deseja gastar?"))
data = str(input("Que dia você irá?"))
if orcamento >= 5000:
    print(f"Você pode ir para{local} no dia{data}")
else:
    print(f"Você não pode ir para{local} no dia{data}")
    