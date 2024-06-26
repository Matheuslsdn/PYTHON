#atividade 11

capital = float(input("Qual o valor inicial? "))
juros = float(input("Qual a taxa de juros anual? "))
tempo = int(input("Quantos anos? "))

print(f"o montante final será de {capital + (capital * (juros / 100) * tempo)}")
