cpf_sujo = input("CPF: ")
cpf_limpo = cpf_sujo.replace(".", "").replace("-", "")
verificacao = []
mult = 1

if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
    print("CPF inválido")

else:
    cpf = tuple(map(int, cpf_limpo))
    for i in cpf:
        if mult == 10:
            break

        else:
            verificacao.append(mult*i)
            mult += 1

    resultado = sum(verificacao) % 11
    cpf = cpf[:-1]
    mult = 0
    verificacao2 = []

    for n in cpf:
        verificacao2.append(mult*n)
        mult += 1
        
    resultado2 = sum(verificacao2) % 11
    cpf = tuple(map(int, cpf_limpo))

    if resultado == cpf[9] and resultado2 == cpf[10]:
        print("CPF VÁLIDO")

    else: 
        print("CPF INVÁLIDO")

    
