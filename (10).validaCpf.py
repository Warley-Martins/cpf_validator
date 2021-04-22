"""
variaveis utilizadas traduzidas:
    message => mensagem
    main => principal
    menu => menu
    Option => opcao
    mainMenuOption => opcao Menu Principal
    validate => validar
"""


def secondValidate(cpf):
    index = 11
    sumValues = 0
    position = 0
    while index >= 2:
        if cpf[position].isnumeric():
            sumValues += int(cpf[position]) * index
            index -= 1
        position += 1
    numValidade = (sumValues * 10) % 11
    print(numValidade)
    if numValidade == 11 or numValidade == 10:
        numValidade = 0
    if str(numValidade) == cpf[13]:
        return True
    return False


def firstValidate(cpf):
    index = 10
    sumValues = 0
    position = 0
    while index >= 2:
        if cpf[position].isnumeric():
            sumValues += int(cpf[position]) * index
            index -= 1
        position += 1
    numValidade = (sumValues * 10) % 11
    print(numValidade)
    if numValidade == 11 or numValidade == 10:
        numValidade = 0
    if str(numValidade) == cpf[12]:
        return True
    return False


def validateFormatCpf(cpf):
    if cpf[3] != "." and cpf[7] != "." and cpf[11] != "-":
        return False
    return True


def formatCpf(cpf):
    position = 0
    cpfFormat = []
    while position < 11:
        if position == 3:
            cpfFormat.append(".")
        elif position == 6:
            cpfFormat.append(".")
        elif position == 9:
            cpfFormat.append("-")
        cpfFormat.append(cpf[position])
        position += 1
    return "".join(cpfFormat)


def inputCpf():
    while True:
        cpf = input("digite o cpf para validação: ")
        if len(cpf) == 11:
            cpf = formatCpf(cpf)
            break
        elif len(cpf) == 14 and validateFormatCpf(cpf):
            break
        else:
            print("\nO CPF informado está com formatação invalida, tente novamente!")
    return cpf


def appValidateCpf():
    cpf = inputCpf()
    print(cpf)
    if firstValidate(cpf):
        if secondValidate(cpf):
            print("\nO cpf ", cpf, " é valido!")
            return
    print("\nO cpf ", cpf, " não é valido!")


def inputInt(message):
    quantity = 0
    while True:
        try:
            if quantity > 5:
                print("\nQuantidade máxima de tentativas excedida, encerrando seção!\n")
                exit()
            return int(input(message))
        except Exception:
            print("\nO valor informado está inválido\n")
            quantity += 1


def menuMain():
    return (
        "\n\tMenu Principal\t"
        + "\nDigite a opção desejada:"
        + "\n(1). Entrar com um cpf para validação"
        + "\n(0). Encerrar"
        + "\nOpção sesejada: "
    )


while True:
    mainMenuOption = inputInt(menuMain())
    if mainMenuOption == 1:
        appValidateCpf()
    elif mainMenuOption == 0 or mainMenuOption == None:
        print("\nPrograma Encerrado\n")
        exit()
    else:
        print("\nOpção invalida\n")
