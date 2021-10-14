# zad 1
def spajacz(pimienia, nazwisko):
    return f'{pimienia}. {nazwisko}'


print(spajacz('N', 'Oszejko'))

# zad 2


def spajacz2(imie, nazwisko):
    return f'{imie[0].capitalize()}. {nazwisko.capitalize()}'


print(spajacz2('Nikita', 'Oszejko'))

# zad 3


def cos(rok2p, rok2o, wiek):
    return int(str(rok2p) + str(rok2o)) - wiek


print(cos(20, 21, 21))

# zad 4


def cosiek(imie, nazwisko, spajacz):
    return spajacz(imie, nazwisko)


print(cosiek('Nikita', 'Oszejko', spajacz2))

# zad 5


def mamale(a, b):
    if b == 0 or a < 0 or b < 0:
        return 'Złe dane'
    return a / b


print(mamale(-5, 0))

# zad 6

# suma = 0
#
# while(suma <= 100):
#     suma += int(input('Podaj kolejna liczbe: '))
#
# print('Osiagnieto lub przekroczono sume liczbe rowną 100.')

# zad 7


def lista_cos(lista):
    return tuple(lista)


lista = [1, 2, 3, 4, 5]

print(lista_cos(lista))


# zad 8

# lista_1 = []
#
# for i in range(10):
#     print('Wprowadz element do listy: ')
#     lista_1.append(input())
#
# lista_1 = tuple(lista_1)
# print(lista_1)


# zad 9


def arytm(a: int):
    lista_dni = ['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
    return lista_dni[(a - 1) % 7]


print(arytm(5))


# zad 10


def funkcja_10(ciag: str):
    return ciag == ciag[::-1]

print(funkcja_10('Kolo'))





