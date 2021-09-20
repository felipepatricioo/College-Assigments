#funcao que recebe dois parametros e retorna o nome mais o email como uma variavel
def funcao1(nome, sobrenome):
    final = nome[0].lower() + sobrenome.lower() + '41' + '@algoritmos.com.br'#foi utilizado a funcao ".lower()" para que independente do input do usuario o email completamente em letras minusculas
    return final
    
#input de nome e sobrenome pelo usuario
nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')
#resultado como pedido no enunciado:
print(f"Sr(a).{(nome.capitalize() + ' ' + sobrenome.capitalize())} seu email é: ", funcao1(nome, sobrenome))#foi utilizado o metodo ".capitalize()" para que independente do input do usuario a primeira letra do seu nome e sobrenome fiquem em maiusculo no print final
