def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 65 > idade >= 18:
        return f'Tem {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Tem {idade} anos: VOTO OPCIONAL'
    else:
        return f'Tem {idade} anos: NÃO VOTA'


nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
