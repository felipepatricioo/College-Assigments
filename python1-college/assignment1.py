#Code a program that receives a student name and final grade
#Laço inifinito que só ira parar de cadastrar dados de alunos quando digitado "0"
while True:
    start = int(input('Inserir dados do aluno? (1 = Sim, 0 = Não) '))
    if start == 0:
        print('Encerrando Programa...')
        break
    
    
    name = input("Nome do aluno: ")#variavel que define o nome do aluno
    grade = float(input("Nota final: "))#variavel que define a nota do aluno (esta sendo convertida para float pois a nota pode sr um numero decimal)

#verificação se a nota dos alunos corresponem ao parametro mostrado no enunciado do exercicio
    if (grade <= 2.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito E'.format(name, grade))
    if (grade >= 3) and (grade <= 4.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito D'.format(name, grade))
    if (grade >= 5) and (grade <= 6.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito C'.format(name, grade))
    if (grade >= 7) and (grade <= 8.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito B'.format(name, grade))
    if (grade >= 9) and (grade <= 10):
        print('O aluno {} tirou nota {} e se enquadra no conceito A'.format(name, grade))
