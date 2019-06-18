a = input('Telefonou para a vitima? ')
b = input('Esteve no local do crime? ')
c = input('Mora perto da vitima? ')
d = input('Devia a vitima? ')
e = input('Já trabalhou com a vitima? ')
resposta = 0

if a == 'sim':
    resposta = resposta + 1
if b == 'sim':
    resposta = resposta + 1
if c == 'sim':
    resposta = resposta + 1
if d == 'sim':
    resposta = resposta + 1
if e == 'sim':
    resposta = resposta + 1

if resposta == 2:
    print ('Suspeita')
if (resposta == 3) or (resposta == 4):
    print ('Cúmplice')
if resposta == 5:
    print ('Assasino')
elif (resposta == 1) or (resposta == 0):
    print ('inocente')
