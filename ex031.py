distancia = float(input('Quantos km foram andados na viagem? '))
preco = float
if distancia <= 200:
    preco = distancia * 0.5
    print('O valor cobrado será: R${}'.format(preco))
else:
    preco = distancia * 0.4
    print('O valor cobrado será: R${}'.format(preco))
