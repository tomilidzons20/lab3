import random
from ciagi import *

# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1 - x: x ∈ < 1, 10 >}
# B = {1, 4, 16,…, 4^7}
# C = {x: x ∈ B i x jest liczbą podzielną przez 2}

print("Zad1")
A = [1 - x for x in range(1, 10)]
print(A)
B = [4**x for x in range(8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)

# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python Comprehension zdefiniuj nową listę,
# która będzie zawierała tylko parzyste elementy

print("Zad2")
lista1 = [random.randint(0, 50) for x in range(10)]
print(lista1)
lista2 = [x for x in lista1 if x % 2 == 0]
print(lista2)

# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartośc - jednostka
# jakiej sie je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie
# będą produkty, których wartość to sztuki

print("Zad3")
slownik1 = {"Papryka": "Kg",
            "Bułki": "Sztuki",
            "Woda": "L",
            "Chleb": "Sztuki",
            "Cola": "L",
            "Kiełbasa": "Sztuki"}
print(slownik1)

slownik2 = {key: value for key, value in slownik1.items() if value == "Sztuki"}
print(slownik2)

# Zad4
# Zdefiniuj funckje, ktora sprawdzi czy trojkat jest prostokatny


def tr_prost(a, b, c):
    if a**2 + b**2 == c**2:
        print("jest prostokatny")
        return 1
    elif a**2 + c**2 == b**2:
        print("jest prostokatny")
        return 1
    elif b**2 + c**2 == a**2:
        print("jest prostokatny")
        return 1
    else:
        print("nie jest prostokatny")
        return 0


print("Zad4")
print(tr_prost(1, 2, 3))
print(tr_prost(3, 5, 4))
print(tr_prost(10, 6, 8))

# Zad5
# Zdefiniuj funkcje ktora policzy pole trapezu. Funckja ma przyjmowac wartosci domyslne


def p_trap(a=0, b=0, h=0):
    poletrap = ((a + b) * h) / 2
    return poletrap


print("Zad5")
print(p_trap())
print(p_trap(2, 4, 5))
print(p_trap(1, 1, 8))

# Zad6
# Zdefiniuj funkcje ktora bedzie liczyc iloczyn elementow ciagu
# Parametry funkcji a(wartosc poczatkowa), b(wielkosc o ile mnozone sa kolejne elementy)
# ile(ile elementow ma mnozyc)
# Ponadto funkcja niech przyjmuje wartosci domyslne: a = 1, b = 4, ile = 10


def ilocz_el(a=1, b=4, ile=10):
    lista3 = []
    for i in range(a, ile + a):
        lista3.append(i * b)
    return lista3


print("Zad6")
print(ilocz_el())
print(ilocz_el(2, 3, 8))

# Zad7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.


def ilocz_el1(* liczby):
    if len(liczby) != 3:
        print("Podaj 3 liczby: poczatkowa, liczbe o ktora ma mnozyc, ile razy ma liczyc")
        return 0
    else:
        lista4 = []
        for i in range(liczby[0], liczby[2] + liczby[0]):
            lista4.append(i * liczby[1])
        return lista4


print("Zad7")
print(ilocz_el1())
print(ilocz_el1(4, 3, 8))

# Zad8
# Napisz funkcję, która wykorzystuje symbol **.
# Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa produktu a wartość to jego koszt.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.


def zakupy(** rzeczy):
    wartosc = 0
    ilosc = len(rzeczy.items())
    for i in rzeczy.values():
        wartosc += i
    return ilosc, wartosc


print("Zad8")
print(zakupy(cola=7, chipsy=5, pizza=20, kabanosy=8))

# Zad9
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami arytmetycznymi
# a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.

print("Zad9")
print("Arytmetyczny ntywyraz:", arytmetyczny.ntywyraz(2, 5, 8))
print("Arytmetyczny suma:", arytmetyczny.suma(2, 8, 4))
print("Geometryczny ntywyraz:", geometryczny.ntywyraz(2, 5, 8))
print("Geometryczny suma:", geometryczny.suma(2, 5, 6))
