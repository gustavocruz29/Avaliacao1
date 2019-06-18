lista = []
media=0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
c = 0
aluno7 = 0
while (c < 10):
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a qyarta nota: '))
    print ('------------------------------------')
    media= (n1+n2+n3+n4)/4
    lista.append(media)
    if media>=7:
        aluno7 = aluno7 + 1
    c = c+1
print ('A media dos alunos: ',lista)
print ('A quantidade de alunos com media maior que 7 é:',aluno7)
