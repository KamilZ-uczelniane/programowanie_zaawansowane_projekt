import socket
import threading
import time
from server import Serwer
from network import wyslij_tekst, odbierz_tekst

def test_odrzucenia_nadmiarowego_klienta():
    
    serwer = Serwer()
    watek_serwera = threading.Thread(target=serwer.start, daemon=True)
    watek_serwera.start()
    time.sleep(0.2) 
    
    klient1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    klient2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    klient3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        klient1.connect(("127.0.0.1", 50000))
        wyslij_tekst(klient1, "1")
        status1 = odbierz_tekst(klient1)
        
        klient2.connect(("127.0.0.1", 50000))
        wyslij_tekst(klient2, "2")
        status2 = odbierz_tekst(klient2)
        
        klient3.connect(("127.0.0.1", 50000))
        wyslij_tekst(klient3, "3")
        status3 = odbierz_tekst(klient3)
        
        assert status1 == "OK"
        assert status2 == "OK"
        assert status3 == "REFUSED"
    finally:

        klient1.close()
        klient2.close()
        klient3.close()