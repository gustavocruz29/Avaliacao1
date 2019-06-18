salario = float (input('Seu salario: '))
if salario <= 280:
    aumento = salario*0.20
    novoSalario = salario+aumento
    print ('O salario antes do reajuste:R$',salario)
    print ('O percentual de aumento:20%')
    print ('O aumento foi de:R$',aumento)
    print ('O novo salario é:R$',novoSalario)
elif (salario > 280)and(salario < 700):
    aumento = salario*0.15
    novoSalario = salario+aumento
    print ('O salario antes do reajuste:R$',salario)
    print ('O percentual de aumento:15%')
    print ('O aumento foi de:R$',aumento)
    print ('O novo salario é:R$',novoSalario)
elif (salario >= 700)and(salario < 1500):
    aumento = salario*0.1
    novoSalario = salario+aumento
    print ('O salario antes do reajuste:R$',salario)
    print ('O percentual de aumento:10%')
    print ('O aumento foi de:R$',aumento)
    print ('O novo salario é:R$',novoSalario)
elif (salario >= 1500):
    aumento = salario*0.05
    novoSalario = salario+aumento
    print ('O salario antes do reajuste:R$',salario)
    print ('O percentual de aumento:5%')
    print ('O aumento foi de:R$',aumento)
    print ('O novo salario é:R$',novoSalario)
