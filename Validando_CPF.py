cpf = input('Digite o CPF: ')
cpf = [int(num) for num in cpf if num.isnumeric()]
novo_cpf = [cpf[i] for i in range(0, 9)]

m1 = m2 = int()
soma_m1 = soma_m2 = int()

if len(novo_cpf) == 9:
    for p, v in enumerate(range(len(novo_cpf) + 1, 1, -1)):
        m1 = v*novo_cpf[p]
        soma_m1 += m1
    formula = 11 - (soma_m1 % 11)
    if formula > 9:
        novo_cpf.append(0)
    else:
        novo_cpf.append(formula)
if len(novo_cpf) == 10:
    for p, v in enumerate(range(len(novo_cpf) + 1, 1, -1)):
        m2 = v*novo_cpf[p]
        soma_m2 += m2
    formula = 11 - (soma_m2 % 11)
    if formula > 9:
        novo_cpf.append(0)
    else:
        novo_cpf.append(formula)

repetidos = set(novo_cpf)
print('O CPF é válido.' if cpf == novo_cpf and len(repetidos) != 1 else 'O CPF é inválido.')
