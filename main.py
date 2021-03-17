cont = True

pratos = {}
pratos['massa'] = ['lassanha']
pratos['outros'] = ['bolo de chocolate']

def toAskWithYesOrNo(question):
    validation = True
    res = None

    while validation:
        res = str(input(question + ' [S/N]'))
        if res == 'S' or res == 'N':
            validation = False

    if res == 'S':
        return True
    else:
        return False

def toAskWithValue(question):
    return str(input(question))

def right():
    print('Acertei de novo\n')

def run():
    input('Pense em um prato que gosta')

    for tipo in pratos:
        tipoIs = toAskWithYesOrNo(f'O prato que você pensou é {tipo}')

        if tipoIs:
            for prato in pratos[f'{tipo}']:
                pratoIs = toAskWithYesOrNo(f'O prato que você gosta é {prato}')

                if pratoIs:
                    right()
                    break
                else:
                    value = toAskWithValue(f'Qual é o prato que você pensou?')
                    pratos[f'{tipo}'].append(value)
                    break
            break
        else:
            newPrato = toAskWithValue(f'Qual é o prato que você pensou?')
            newTipo = toAskWithValue(f'Qual o tipo dele?')

            pratos[newTipo].append(newPrato)

    return True

while cont:
    cont = run()