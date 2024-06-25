#prática 1

nome = "Tim Tester"
idade = 20
skill1 = "python"
level1 = "iniciante"
skill2 = "java"
level2 = "senior"
skill3 = "C++"
level3 = "pleno"
baixo = 2000
alto = 3000

print("meu nome é ", nome, "tenho", idade ,"anos")
print("minhas habilidades são:")
print(skill1, ":", level1)
print(skill2, ":", level1)
print(skill3, ":", level1)

print("Procuro um emprego com um salário de", baixo, "a", alto, "euros por mês")

#Atividade 01

nome = "Steve"
apelido = "Sanders"
endereco = "Rua x"
codPostal = 83225456

print(nome,apelido,endereco,codPostal)

nome1 = input("Qual é o seu nome?")
apelido1 = input("Qual é o seu apelido?")
endereco1 = input("Qual é o seu endereço?")
codPostal1 = input("Qual é o seu código postal?")

print(nome1, apelido1, endereco1, codPostal1)

#aividade 02

nome2 = input("Por favor digite um nome:")
ano2 = input("Por favor digite um ano:")

print(nome2, "é um(a) viajante cavaleira, nascida no ano", ano2)
print("Certa manhã,", nome2, "acordou com um barulho terrível: um dragão se proxima da aldeia.")
print("Somente", nome2, "poderia salvar os moradores da aldeia.")

#atividade 03

cidade = "São Paulo"
print(cidade)
cidade = input("Escreva o nome da nova cidade")
print("Agora a cidade é", cidade)

#atividade 04

string = input("adicione um texto á string:")
inteiro = input("escreva um número inteiro:")
float = input("escreva um número racional")

print(string, "string")
print(inteiro, "inteiro")
print(float, "float")

#Atividade 05

frase1 = "aqui estou mais um dia"
frase2 = "sobre o olhar sanguinário do vigia"

print(frase1, "" + frase2)

ano = int(input("coloque aqui seu ano de nascimento:"))
print(f"Ao fim de 2024 você terá: {2024 - ano} ")

altura = float(input("Qual a sua altura?"))
peso = float(input("Qual o seu peso"))

let = peso / (altura / 100) * 2

print(f"Seu IMC é: {let}")
