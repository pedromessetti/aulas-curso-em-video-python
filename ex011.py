def cidade():
    city = str(input('\nDigite o nome de uma cidade: '))
    min = city.lower()
    if 'santo' in min:
        print('A cidade {} tem nome de santo.'.format(city.title().strip()))
        return True
    if 'são' in min:
        print('A cidade {} tem nome de santo.'.format(city.title().strip()))
        return True
    if 'santa' in min:
        print('A cidade {} tem nome de santa.'.format(city.title().strip()))
        return True
    if 'sao' in min:
        print('A cidade {} tem nome de santo.'.format(city.title().strip()))
        return True
    if 'nossa senhora' in min:
        print('A cidade {} tem nome de santa.'.format(city.title().strip()))
        return True
    else:
        print('A cidade {} não tem nome de santo ou santa.'.format(city.title().strip()))
        return True
cidade()