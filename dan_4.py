# Strukture podataka

# brojevi = [-9, 3, 11, 4, 3, -9, 4, 1]
# print(brojevi)

# skup = set(brojevi)
# print(skup)

# # recnik = {
# #     id: 1
# # }

# # print(recnik.get(id))

# skup_studenata = set([
#     2020100900,
#     2020100902,
#     2020100903,
#     2020100904,
#     2020100906
# ])

# skup_prijava_za_ispit = set([
#     2020100903,
#     2020100904,
#     2022800700
# ])

# moji_studenti = skup_studenata.intersection(skup_prijava_za_ispit)
# print(moji_studenti)

# for indeks in moji_studenti:
#     print(indeks)

# brojevi = [-9, 3, 11, 4, 3, -9, 4, 1]
# print(brojevi)

# ntorka = tuple(brojevi)

# print(ntorka)

# for el in ntorka:
#     print(el)

# print(ntorka.count(-9))
# print(ntorka.index(11))

# skup_studenata = set([
#     2020100900,
#     2020100902,
#     2020100903,
#     2020100904,
#     2020100906
# ])

# skup_prijava_za_ispit = set([
#     2020100903,
#     2020100904,
#     2022800700
# ])

# moji_studenti = skup_studenata.intersection(skup_prijava_za_ispit)
# print(moji_studenti)

# moji_studenti = list(moji_studenti)
# print( moji_studenti)

# ntorka = tuple([1, 2, 3, 2, 1, 2])
# print(ntorka)

# brojevi = list(ntorka)
# print(brojevi)
# brojevi.sort()
# print(brojevi)

# import collections

# Student = collections.namedtuple("Student", "ime, prezime")
# student_1 = Student("Milan", "Tair")
# print(student_1)
# print(student_1.ime)

# korisnici = [
#     { "id": 1, "korisnik": "Mirko", "email": "mirko@gmail.com" },
#     { "id": 2, "korisnik": "Milan", "email": "milan@gmail.com" },
#     { "id": 3, "korisnik": "Divna", "email": "divna@gmail.com" },
#     { "id": 4, "korisnik": "Milica", "email": "milica@gmail.com" }
# ]

# for korisnik in korisnici:
#     print(korisnik)
#     print(korisnik["id"])
#     print(f"Korisnikovo ime je: {korisnik['korisnik']}")

# Program radi sa podacima o studentima.
# Ima osnovne informacije o studentima (lista).
# Za svakog studenta ima listu brojeva bodova na predmetima.
# Program treba da izracuna prosecnu ocenu i da prikaze tabelu svih studenata poredjanu po ocenama (10, 9, ... 6, pao) i da prikaze prosek svih ocena.

import collections

Student = collections.namedtuple("Student", "indeks, ime, prezime, predmeti")
Zapis_predmeta = collections.namedtuple("Zapis_predmeta", "predmet, bodovi")

studenti = [
    Student(2022900800, "Pera", "Peric", [
        Zapis_predmeta("Informatika", 82),
        Zapis_predmeta("Engleski jezik 1", 91),
        Zapis_predmeta("Osnove programiranja - Python", 69),
        Zapis_predmeta("Menadzment", 37)
    ]),
    Student(2022900800, "Milica", "Milic", [
        Zapis_predmeta("Informatika", 90),
        Zapis_predmeta("Engleski jezik 1", 100),
        Zapis_predmeta("Osnove programiranja - Python", 80),
        Zapis_predmeta("Menadzment", 27)
    ]),
    Student(2022900800, "Teodor", "Teodorovic", [
        Zapis_predmeta("Baze podataka", 50),
        Zapis_predmeta("Projektovanje informacionih sistema", 92)
    ])
]

Zapis_ocene = collections.namedtuple("Zapis_ocene", "predmet, bodovi, ocena")

def obradi_zapis_predmeta (zp):

    if zp.bodovi < 51:
        ocena = 5
    elif zp.bodovi < 61:
        ocena = 6
    elif zp.bodovi < 71:
        ocena = 7
    elif zp.bodovi < 81:
        ocena = 8
    elif zp.bodovi < 91:
        ocena = 9
    else:
        ocena = 10
    return Zapis_ocene(zp.predmet, zp.bodovi, ocena)

def vrati_za_sort (predmet):
    return predmet.bodovi

def stampaj_podatke_o_studentu (s):
    suma = 0
    broj_pozitivnih_ocena = 0

    print(f"{s.indeks} - {s.ime} - {s.prezime}")

    s.predmeti.sort(key = vrati_za_sort, reverse = True)

    for op in s.predmeti:
        zo = obradi_zapis_predmeta(op)
        ocena = zo.ocena

        if ocena > 5:
            suma += ocena
            broj_pozitivnih_ocena += 1

        if ocena == 5:
            ocena = "pao"
        else:
            ocena = str(ocena)

        print(f"    {zo.predmet:40s} {ocena:>3}")

    prosek = suma / broj_pozitivnih_ocena

    print(f"    Prosecna ocena: {prosek:.2f}")
    print()

for student in studenti:
    stampaj_podatke_o_studentu(student)