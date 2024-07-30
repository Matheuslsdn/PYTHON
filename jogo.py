import random

class Monstro:
    def __init__(self, nivel):
        self.nivel = nivel
        self.hp = 20 * nivel
        self.exp = 3 * nivel
    
    def __str__(self):
        return f"Monstro Nível {self.nivel} - HP: {self.hp}"

def gerar_monstros(andar):
    min_nivel = andar
    max_nivel = andar * 5
    
    if andar <= 10:
        quantidade = random.randint(1, 100)
    elif andar <= 20:
        quantidade = random.randint(25, 150)
    elif andar <= 30:
        quantidade = random.randint(50, 200)
    elif andar <= 40:
        quantidade = random.randint(75, 250)
    else:
        quantidade = random.randint(250, 1000)
    
    return [Monstro(random.randint(min_nivel, max_nivel)) for _ in range(quantidade)]

def calcular_exp_para_proximo_nivel(nivel):
    return 50 * (3 ** (nivel - 1))

def iniciar_jogo():
    moedas = 0.0
    exp_total = 0
    nivel_jogador = 1
    andar_atual = 1
    dano_base = 5
    monstros_derrotados = {}

    while andar_atual <= 50:
        print(f"\nVocê está no andar {andar_atual}.")
        monstros = gerar_monstros(andar_atual)
        print(f"Você encontrou {len(monstros)} monstros!")
        
        for monstro in monstros:
            print(f"\nVocê encontrou um {monstro}!")
            
            while monstro.hp > 0:
                ataque = random.randint(dano_base, dano_base + 10)
                monstro.hp -= ataque
                print(f"Você atacou o monstro causando {ataque} de dano. HP do monstro: {max(monstro.hp, 0)}")
                
                if monstro.hp <= 0:
                    moedas_ganhas = monstro.nivel * 0.001
                    moedas += moedas_ganhas
                    print(f"Você derrotou o monstro e ganhou {moedas_ganhas:.3f} moedas! Total de moedas: {moedas:.3f}")
                    
                    if monstro.nivel not in monstros_derrotados:
                        monstros_derrotados[monstro.nivel] = 0
                    
                    if monstros_derrotados[monstro.nivel] == 0:
                        exp_ganha = monstro.exp * 2
                    else:
                        exp_ganha = monstro.exp
                    
                    exp_total += exp_ganha
                    monstros_derrotados[monstro.nivel] += 1
                    print(f"Você ganhou {exp_ganha} EXP! Total de EXP: {exp_total}")
        
        print(f"\nVocê limpou o andar {andar_atual}!")

        while True:
            print("\nMenu:")
            print("1. Subir para o próximo andar")
            print(f"2. Repetir o andar {andar_atual}")
            if andar_atual > 1:
                print(f"3. Descer para o andar {andar_atual - 1}")
            print("4. Subir de nível")
            escolha = input("Escolha uma opção: ").strip()

            if escolha == '1':
                andar_atual += 1
                break
            elif escolha == '2':
                break
            elif escolha == '3' and andar_atual > 1:
                andar_atual -= 1
                break
            elif escolha == '4':
                exp_necessaria = calcular_exp_para_proximo_nivel(nivel_jogador)
                if exp_total >= exp_necessaria:
                    exp_total -= exp_necessaria
                    nivel_jogador += 1
                    dano_base += 5
                    print(f"Você subiu para o nível {nivel_jogador}! Novo dano base: {dano_base}. EXP restante: {exp_total}.")
                else:
                    print(f"EXP insuficiente! Você precisa de {exp_necessaria - exp_total} EXP a mais para subir de nível.")
            else:
                print("Escolha inválida. Por favor, tente novamente.")
        
        if andar_atual > 50:
            break

    print(f"Parabéns! Você completou todos os 50 andares e acumulou {moedas:.3f} moedas e {exp_total} EXP. Até a próxima!")

if __name__ == "__main__":
    print("Bem-vindo ao Jogo de Monstros e Moedas!")
    iniciar_jogo()
