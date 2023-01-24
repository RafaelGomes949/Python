cpf = input('Digite um CPF: ')
listaoricpf = list(cpf)
novo_cpf = cpf[:-2]
listacpf = list(novo_cpf)

emaior = 0
i = 0
acumulativa = 0
resultado = 0

j = 0
acumulativa2 = 0
resultado2 = 0

for multiplicadores in range(10, 1, -1):
    resultado = (int(listacpf[i]) * multiplicadores)
    i = i + 1
    acumulativa = acumulativa + resultado

emaior = (11 - (acumulativa % 11))
if emaior > 9:
    listacpf.append('0')
else:
    listacpf.append(str(emaior))

for multiplicadore in range(11, 1, -1):
    resultado2 = (int(listacpf[j]) * multiplicadore)
    j = j + 1
    acumulativa2 = acumulativa2 + resultado2

emaior2 = (11 - (acumulativa2 % 11))
listacpf.append(str(emaior2))

if listaoricpf == listacpf:
    print('Válido')
else:
    print('Inválido')

#if cpf == novo_cpf:
#    print('Válido')
#else:
#    print('Inválido')




#digitos = CPF.split('.')
#split = digitos[2]
#traco = digitos[2].split('-')
#print(digitos[0])
