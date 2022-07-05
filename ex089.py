from time import sleep


def cores(cor):
    if cor == 'amarelo':
        print('\033[1;33m', end='')
    if cor == 'vermelho':
        print('\033[1;31m', end='')
    if cor == 'limpa':
        print('\033[1m', end='')
    if cor == 'azul':
        print('\033[1;34m', end='')
    if cor == 'verde':
        print('\033[1;32m', end='')
    if cor == 'branco':
        print('\033[1;97m', end='')
    if cor == 'amareloclaro':
        print('\033[1;93m', end='')


def lin(qntdl):
    cores('amareloclaro')
    print('-'*qntdl)
    cores('branco')


def escolha():
    lin(50), print(f'''{"[0] - Encerrar o programa":^50}\n{"[1] - Digitar nova matéria":^50}
{"[2] - Mostrar boletim":>33}'''), lin(50)
    op = int(input('Digite a opção: '))
    while op != 0 and op != 1 and op != 2:
        sleep(1)
        cores('vermelho')
        print('Digitação inválida!')
        cores('branco')
        op = int(input('Digite (0 ou 1 ou 2): '))
    if op == 0:
        return op
    if op == 1:
        return op
    if op == 2:
        return op


contn = media = 0
alunos = []
notas = []
boletim = []
materias = []
lin(50)
print('{:^50}'.format('Cadastro do aluno'))
lin(50)
cores('branco')
alunos.append(str(input('Nome Completo: ')).strip().title())
boletim.append(alunos)
lin(50)
materias.append(str(input('Digite a matéria: ')).strip().title())
boletim.append(materias)
lin(50)
for n in range(1, 5):
    nota = float(input(f'Nota {n}° Bimestre: '))
    media += nota
    while 0 > nota or nota > 10:
        sleep(1)
        print('Digitação inválida!')
        sleep(1)
        nota = float(input(f'Nota {n}° Bimestre: '))
    notas.append(nota)
media /= 4
notas.append(media)
boletim.append(notas)
lin(50)
print(f'Notas de {materias[-1]} de {alunos[-1]} salvas!')
resp = escolha()
while resp == 1:
    lin(50)
    materias.append(str(input('Digite a matéria: ')).strip().title())
    lin(50)
    media = 0
    for n in range(1, 5):
        nota = float(input(f'Nota {n}° Bimestre: '))
        media += nota
        while 0 > nota or nota > 10:
            sleep(1)
            print('Digitação inválida!')
            sleep(1)
            nota = float(input(f'Nota {n}° Bimestre: '))
        notas.append(nota)
    media /= 4
    notas.append(media)
    boletim.append(notas)
    lin(50)
    print(f'Notas de {materias[-1]} de {alunos[-1]} salvas!')
    resp = escolha()
if resp == 2:
    lin(50)
    print('{:^50}'.format(f'Boletim de {alunos[-1]}'))
    lin(50)
    print(f'{"Matéria":^12} |1° Bi||2° Bi||3° Bi||4° Bi||Média|')
    for ele in range(0, len(materias)):
        print(f'{materias[ele]:12} ', end='')
        for g in range(0, 5):
            print(f'| {boletim[2][g]:.1f} |', end='')
            contn += 1
        if contn % 5 == 0:
            print('')
            del notas[0]
            del notas[0]
            del notas[0]
            del notas[0]
            del notas[0]
    lin(50)
if resp == 0:
    lin(50)
    sleep(1)
    print('Encerrando programa...')
    sleep(1.5)
