import socket

from network import wyslij_tekst, odbierz_tekst, odbierz_obiekt
from models import Kot, Pies, Ksiazka

OCZEKIWANE_TYPY = {
    "kot": Kot,
    "pies": Pies,
    "ksiazka": Ksiazka
}

def uruchom_klienta(id_klienta):
    gniazdo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        gniazdo.connect(("127.0.0.1", 50000))
        
        wyslij_tekst(gniazdo, str(id_klienta))
        status = odbierz_tekst(gniazdo)
        
        if status == "REFUSED":
            print(f"[Klient {id_klienta}] Otrzymano REFUSED: Serwer jest pełny. Kończę.")
            return 
            
        print(f"[Klient {id_klienta}] Połączono! Status serwera: {status}")
        
       
        zapytania = ["kot", "pies", "samochod"]
        
        for nazwa_klasy in zapytania:
            print(f"\n[Klient {id_klienta}] Proszę o klasę: {nazwa_klasy}")
            wyslij_tekst(gniazdo, f"GET {nazwa_klasy}") 
            
            
            odebrana_lista = odbierz_obiekt(gniazdo)
            
            
            typ_docelowy = OCZEKIWANE_TYPY.get(nazwa_klasy)
            
           
            def sprawdz_i_rzutuj(obiekt):
                
                if typ_docelowy is None or not isinstance(obiekt, typ_docelowy):
                    raise TypeError(f"Błąd rzutowania! Oczekiwano {nazwa_klasy}, a otrzymano {type(obiekt).__name__}")
                return obiekt

            try:
                
                strumien = map(sprawdz_i_rzutuj, odebrana_lista)
                
                
                for poprawny_obiekt in strumien:
                    print(f"[Klient {id_klienta} ODEBRANO]: {poprawny_obiekt}")
                    
            except TypeError as blad:
                
                print(f"[Klient {id_klienta} BŁĄD]: {blad}")
        
        
        wyslij_tekst(gniazdo, "QUIT")
        
    except ConnectionRefusedError:
        print("Nie udało się połączyć – czy serwer jest włączony?")
    finally:
        gniazdo.close()

if __name__ == "__main__":
    
    uruchom_klienta(123)