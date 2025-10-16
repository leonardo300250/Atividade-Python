nome = input('Digite Seu Nome: ')
print("Seja Bem Vindo Jogador(a): {}".format(nome))

respCerta = 10

tentativa = int(input('Tente advinhar o Número certo: '))
if tentativa<respCerta:
    print('Você errou o Número e maior, Tente Novamente')
elif tentativa>respCerta:
    print('Você errou o Número é menor, Tente Novamente')
else:
    print('Parabéns Você Acertou!!!')