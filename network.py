import struct
import pickle

def wyslij_tekst(gniazdo, tekst):
    
    gniazdo.sendall((tekst + "\n").encode("utf-8"))

def odbierz_tekst(gniazdo):
    
    dane = bytearray()
    while True:
        kawalek = gniazdo.recv(1)
        if not kawalek or kawalek ==b"\n":
            break
        
        dane.extend(kawalek)
        
    
    return dane.decode("utf-8").strip()

def wyslij_obiekt(gniazdo, obiekt):
    
    bajty = pickle.dumps(obiekt)
    rozmiar = len(bajty)
    
    gniazdo.sendall(struct.pack("!I", rozmiar))

   
    gniazdo.sendall(bajty)

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