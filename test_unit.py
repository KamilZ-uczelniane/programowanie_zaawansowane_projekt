from models import Kot, Pies
from repository import zbuduj_baze, pobierz_obiekt

def test_poprawnosci_equals_w_klasach():

    kot_1 = Kot("Mruczek", 2)
    kot_2 = Kot("Mruczek", 2)
    kot_3 = Kot("Filemon", 1)
    
    assert kot_1 == kot_2
    assert kot_1 != kot_3

def test_czy_baza_tworzy_po_cztery_obiekty():
    baza = zbuduj_baze()
    koty = pobierz_obiekt(baza, "kot")
    psy = pobierz_obiekt(baza, "pies")
    
    assert len(koty) == 4
    assert len(psy) == 4
    assert "kot_1" in baza