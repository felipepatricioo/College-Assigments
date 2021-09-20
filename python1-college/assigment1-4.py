from operator import itemgetter
produtos = {}#dicionario produtos
listaProd = []#lista produtos
print('Cadastro de produtos: (Digite 0 no "codigo do produto" para encerrar o programa.')
while True:
    produtos['codigo'] = int(input('Digite o código do produto:'))
    if (produtos['codigo'] == 0):
        print('Encerrando Programa...')#encerra caso o usuario digite 0 em "código"
        break
    produtos['estoque'] = int(input('Digite o número em estoque do produto:'))
    produtos['minimo'] = int(input('Digite o valor mínimo do estoque do produto:'))
    listaProd.append(produtos.copy())#copia a listaProd em produtos



listaOrdenada = sorted(listaProd, key=itemgetter('codigo'))
print(listaOrdenada)