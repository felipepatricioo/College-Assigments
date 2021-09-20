import random
#criei uma funcao para embaralhar e sortear um nome da lista
def sorteioFunc ():
    random.shuffle(listaSorteio)
    sorteado = random.choice(listaSorteio)
    return sorteado

print('Doações para caridade 2021:')

listaSorteio = []

loop = input('Quer cadastar uma doação?[S/N]')
while True: #loop que continua infinitamente a nao ser q o usuario decida parar de registrar nomes
    x = 0
    if loop.lower() == 's':
        nome = input('Nome do doador:')
        doacao = float(input('Valor da doação:'))
        if doacao >= 10:
            doacaoTotal = doacao/10 #divide o valor doado por 10 para usar o resultado como parametro do proximo laço
            while (x < int(doacaoTotal)):#converti o valor para inteiro para nao dar erro na hora de fazer o loop 
                x += 1
                listaSorteio.append(nome)#adiciona o nome do doador 'x' vezes que o valor doado for divisivel por 10
                
        loop2 = input('Quer cadastrar mais uma doação?[S/N]')#pergunta se o usuario quer cadastrar mais alguem caso contrario > break
        if loop2.lower() == 's' :
            continue
        else:
            print('Encerrando programa...')
            break
    else:
        break 


print('O(a) vencedor(a) do sorteio foi o(a): {}'.format(sorteioFunc()))
print('Lista do sorteio: {}'.format(listaSorteio))
