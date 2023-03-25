from random import choice

numeros = [0, 1, 2, 3, 4, 5]
numero = choice(numeros)
snum = int(input('Qual numero você acha que foi selecionado? '))
if snum == numero:
    print('Parabueins! Você acertou o numero sorteado.')
else:
    print('Você errou! O número sorteado foi {}'.format(numero))
