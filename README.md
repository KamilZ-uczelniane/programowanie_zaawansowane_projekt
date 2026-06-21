Skład zespołu i role:
Kamil Zatorski 167876 - kierownik projektu, podłączenie klienta, test e2e 
Marcin Milczarek 168964 - server, plik network, dokumentacja
Kacper Zbytniewski 168936 - przygotowanie plików models, repository
Kacper Huber 168267 - przygotowanie plików test integration, test unit

Instrukcja uruchomienia:
Pierwszym krokiem jest uruchomienie serwera. W wierszu poleceń przechodzimy do lokalizacji projektu i wpisujemy komendę "python server.py" (do uruchomienia projektu wystarczy czysty python wersja 3.7 lub nowsza), pozostawienie tego okna jest wymagane dla działania reszty plików (z wyłączeniem pliku test_e2e.py, który tworzy własną instancję serwera). Połączenie klienta wykonujemy w nowym oknie terminala, wpisując komendę "python client.py", tak samo robimy jeśli chcemy wykonać testy.


Opis testów:
-test_unit.py - sprawdza poprawnośc porównywania obiektów i generowania bazy danych
-test_integration.py - testuje serializację poprzez utworzenie wirtualnego kabla w pamięci RAM
-test_e2e.py - podłącza 3 klientów i sprawdza czy pierwszych dwóch otrzyma status OK, a trzeci zostanie odrzucony.
Jeżeli test nie zwróci żadnej wartości, oznacza to, że przebiegł on pomyślnie.

Rola AI w tym projekcie:
- Używaliśmy Gemini oraz ChatGPT
- Korzystaliśmy z nich w celu utworzenia komentarzy w plikach, aby inni członkowie grupy wiedzieli o co chodzi w konkretnych fragmentach (usunięte w końcowej fazie)

Przykładowe fragmenty kodu wygenerowane przez AI:

W pliku models ten fragment sprawia, że obiekty są niezmienne:
@dataclass(frozen=True)
class Kot:
    imie: str 
    wiek: int 

W pliku network:
def odbierz_obiekt(gniazdo):
    naglowek = gniazdo.recv(4)
    if not naglowek:
        return None
    rozmiar = struct.unpack("!I", naglowek)[0]

    odberane_dane = bytearray()
    while len(odberane_dane) < rozmiar:
        ile_brakuje = rozmiar - len(odberane_dane)
        kawalek = gniazdo.recv(ile_brakuje)
        odberane_dane.extend(kawalek)

    return pickle.loads(odberane_dane)

W pliku server mieliśmy problem z ogarnięciem jak ograniczyć liczbę klientów i nie wywalić servera:
class Serwer: 
    def __init__(self):
        self.baza = zbuduj_baze()
        self.stoper = threading.Semaphore(MAX_CLIENTS)

    def obsluz_klienta(self, polaczenie, adres):
        czy_wszedl = self.stoper.acquire(blocking=False)

W teście e2e dopisał:
time.sleep(0.2)

