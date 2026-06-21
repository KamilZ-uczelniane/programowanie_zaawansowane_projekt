import socket
import threading
import time
import random

from network import odbierz_tekst, wyslij_tekst, wyslij_obiekt
from repository import zbuduj_baze, pobierz_obiekt

MAX_CLIENTS = 2

class Serwer: 
    def __init__(self):

        self.baza = zbuduj_baze()

        self.stoper = threading.Semaphore(MAX_CLIENTS)

    def obsluz_klienta(self, polaczenie, adres):

        czy_wszedl = self.stoper.acquire(blocking=False)

        with polaczenie: 
            id_klienta = odbierz_tekst(polaczenie)

            if not czy_wszedl:
                print(f"[Serwer] Odrzucono klienta ID {id_klienta} z {adres}")
                wyslij_tekst(polaczenie, "REFUSED")
                return
            
            print(f"[Serwer] Zaakceptowano klienta ID {id_klienta} z {adres}")
            wyslij_tekst(polaczenie, "OK")

            try: 
                while True:
                    zapytanie = odbierz_tekst(polaczenie)
                    if not zapytanie or zapytanie.upper() == "QUIT":
                        break

                    if zapytanie.upper().startswith("GET "):
                        szukany_typ = zapytanie.split(" ")[1]
                        obiekty = pobierz_obiekt(self.baza, szukany_typ)

                        time.sleep(random.uniform(0.5, 1.5))

                        if not obiekty: 
                            obiekty = [next(iter(self.baza.values()))]

                        wyslij_obiekt(polaczenie, obiekty)
                        print(f"[Serwer] Przesłano '{szukany_typ}' do klienta ID {id_klienta}.")

            finally:
                self.stoper.release()

    def start(self):
        gniazdo_serwera = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gniazdo_serwera.bind(("127.0.0.1", 50000))
        gniazdo_serwera.listen()
        print(f"Serwer uruchomiony! Limit klientów: {MAX_CLIENTS}")

        while True: 
            polaczenie, adres = gniazdo_serwera.accept()

            nowy_watek = threading.Thread(target=self.obsluz_klienta, args=(polaczenie,adres), daemon=True)
            nowy_watek.start()

if __name__ == "__main__":
    Serwer().start()
