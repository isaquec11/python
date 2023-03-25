velocidade = float(input('Digite a velocidade do carro: Km '))
multa = float(velocidade-60) * 7
if velocidade > 60:
    print('Você passou a velocidade permitida e foi multado no Valor de: R${:.2f}'.format(multa))
else:
    print('Você passou pelo radar com a velocidade de Km{:.1f}'.format(velocidade))
