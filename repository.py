from models import Kot, Pies, Ksiazka

def zbuduj_baze(): 
    baza = {}

    baza["kot_1"] = Kot(imie="Mruczek", wiek=2)
    baza["kot_2"] = Kot(imie="Puszek", wiek=4)
    baza["kot_3"] = Kot(imie="Filemon", wiek=1)
    baza["kot_4"] = Kot(imie="Klara", wiek=6)

    baza["pies_1"] = Pies(imie="Burek", rasa="Kundel")
    baza["pies_2"] = Pies(imie="Azor", rasa="Owczarek")
    baza["pies_3"] = Pies(imie="Kora", rasa="Beagle")
    baza["pies_4"] = Pies(imie="Mopsik", rasa="Mops")

    baza["ksiazka_1"] = Ksiazka(tytul="Python Od Podstaw", strony=220)
    baza["ksiazka_2"] = Ksiazka(tytul="Sieci Komputerowe", strony=180)
    baza["ksiazka_3"] = Ksiazka(tytul="Wielowątkowość", strony=250)
    baza["ksiazka_4"] = Ksiazka(tytul="Testowanie", strony=140)

    return baza

def pobierz_obiekt(mapa_danych, szukany_typ):
    
    znalezione = []

    prefix = szukany_typ.lower() + "_"
    for klucz, wartosc in mapa_danych.items(): 

        if klucz.startswith(prefix):
            znalezione.append(wartosc)

    return znalezione
