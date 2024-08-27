import random

pontos_maquina = 0
pontos_usuario = 0

escolha_aleatoria = ['p', 't', 'l']

while True:
    escolha = input('Digite P(PEDRA), T(Tesoura), L(Papel) ou Q para sair. ')

    if escolha == 'q':
        break

    if escolha not in escolha_aleatoria:
        continue

    maquina = random.randint(0,2)
    maquina_escolha = escolha_aleatoria[maquina]

    print(f'Escolha da maquina foi {maquina_escolha}')


    if escolha == maquina_escolha:
        print('Empate!!')

    elif escolha == 'p' and maquina_escolha == 't':
        print('Você ganhou !!!')
        pontos_usuario += 1
    
    elif escolha == 't' and maquina_escolha == 'l':
        print('Você ganhou !!!')
        pontos_usuario += 1

    elif escolha == 'l' and maquina_escolha == 'p':
        print('Você ganhou !!!')
        pontos_usuario += 1
    else:
        print('Você perdeu!!!')
        pontos_maquina += 1

if pontos_maquina > pontos_usuario:
    print('Você perdeu!!!!')
    print('Pontos Usuário: ', pontos_usuario)
    print('Pontos Maquina: ', pontos_maquina)

elif pontos_usuario > pontos_maquina:
    print('Você Ganhou!!!!')
    print('Pontos Usuário: ', pontos_usuario)
    print('Pontos Maquina: ', pontos_maquina)

else:
    print('Empate!!!')
    print('Pontos Usuário: ', pontos_usuario)
    print('Pontos Maquina: ', pontos_maquina)


