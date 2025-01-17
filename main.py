import random
import time


# Função para exibir o dia da semana e a hora
def exibir_dia_hora(dia, hora):
def exibir_dia_hora(dia, hora):
    dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado",
                      "Domingo"]
    print(f"\nHoje é {dias_da_semana[dia]}, {hora}:00 horas.")


# Função para gerar perguntas de matemática mais difíceis
def perguntar_trabalho():
    problemas = [
        ("Quanto é 12 * 15?", 180),
        ("Quanto é 225 ÷ 15?", 15),
        ("Raiz quadrada de 256?", 16),
        ("Quanto é 50 + (-30)?", 20),
        ("Quanto é 45 * (-2)?", -90),
        ("Raiz quadrada de 81?", 9)
    ]
    pergunta = random.choice(problemas)
    resposta_usuario = int(input(f"Problema de matemática: {pergunta[0]} "))

    if resposta_usuario == pergunta[1]:
        print("Resposta correta! Você avançou no trabalho.")
        return True
    else:
        print("Resposta incorreta. Tente novamente!")
        return False


# Função para gerenciar as interações com amigos
def conversar_com_amigos():
    amigos = ["Alexandre", "Bruno", "Carlos", "Luana"]
    amigo = random.choice(amigos)
    print(f"\n{amigo} chegou! Ele diz: 'Oi, como você está?'")

    while True:
        print("\nEscolha uma opção para responder:")
        print("1. Oi, tudo bem! E você?")
        print("2. Oi, estou ocupado.")
        print("3. Não tenho tempo agora, estou com pressa.")
        print("4. Sair da conversa")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            print(f"{amigo}: 'Eu estou bem, obrigado! Como vai o trabalho?'")
            break
        elif escolha == 2:
            print(f"{amigo}: 'Entendi, vou te deixar tranquilo.'")
            break
        elif escolha == 3:
            print(f"{amigo}: 'Tudo bem, depois a gente se fala.'")
            break
        elif escolha == 4:
            print(f"{amigo}: 'Até mais então!'")
            break
        else:
            print("Escolha inválida, tente novamente...")


# Função para gerenciar interações com familiares
def conversar_com_familiares():
    familiares = ["Mãe", "Pai", "Avó", "Irmão"]
    familiar = random.choice(familiares)
    print(f"\n{familiar} diz: 'Oi, tudo bem com você?'")

    while True:
        print("\nEscolha uma opção para responder:")
        print("1. Oi, tudo bem! E você?")
        print("2. Eu estou cansado, muito trabalho.")
        print("3. Oi, só queria saber como você está.")
        print("4. Sair da conversa")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            print(f"{familiar}: 'Eu estou ótimo, obrigada por perguntar. Como estão as coisas por aí?'")
            break
        elif escolha == 2:
            print(f"{familiar}: 'Parece que você precisa de uma pausa. Vamos conversar mais tarde.'")
            break
        elif escolha == 3:
            print(f"{familiar}: 'Acho que você está bem. Lembre-se de descansar também.'")
            break
        elif escolha == 4:
            print(f"{familiar}: 'Até logo!'")
            break
        else:
            print("Escolha inválida, tente novamente...")


# Função para simular o trabalho e a rotina do personagem
def rotina_trabalho():
    saldo = 273
    salario = 489.21
    carro_comprado = False
    dia_da_semana = random.randint(0, 6)
    hora = 7

    while hora <= 19:  # O dia só acaba às 19h
        exibir_dia_hora(dia_da_semana, hora)

        # Realiza perguntas de matemática no trabalho
        if hora == 9:
            print("\nHora do trabalho! Vamos começar com algumas perguntas de matemática:")
            while not perguntar_trabalho():
                pass  # Espera até acertar as perguntas para continuar o trabalho

        # Conversa com amigos ou familiares (opcional)
        if hora == 10:
            print("\nVocê pode conversar com seus amigos ou familiares.")
            conversa = input("Você quer conversar com um amigo ou familiar? (s/n): ").strip().lower()
            if conversa == "s":
                escolha = input("Escolha amigo ou familiar: (a) Amigo (b) Familiar: ").strip().lower()
                if escolha == "a":
                    conversar_com_amigos()
                elif escolha == "b":
                    conversar_com_familiares()
                else:
                    print("Escolha inválida.")

        # A cada hora, o tempo avança
        hora += 1

        # Verificar se o saldo é suficiente para o carro
        if saldo >= 3000 and not carro_comprado:
            carro_comprado = True
            print(f"\nVocê comprou o carro! Agora pode viajar e ir para a loja de imóveis!")

        # Fim do dia
        if hora == 19:
            print("\nO dia terminou! Você descansou e está pronto para o próximo dia.")
            break

        # Pausa para o jogador, simula a espera
        time.sleep(1)


# Chamar a função para simular a rotina
rotina_trabalho()
