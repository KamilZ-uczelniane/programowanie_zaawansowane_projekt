import socket
from models import Kot
from network import wyslij_obiekt, odbierz_obiekt

def test_serializacji_przez_siec():
   
    lewy_koniec, prawy_koniec = socket.socketpair()
    
    try:
        wysylane_dane = [Kot("Mila", 2), Kot("Luna", 4)]
        
        wyslij_obiekt(lewy_koniec, wysylane_dane)
        
        odebrane_dane = odbierz_obiekt(prawy_koniec)
        
        assert odebrane_dane == wysylane_dane
    finally:
        lewy_koniec.close()
        prawy_koniec.close()