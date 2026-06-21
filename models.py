from dataclasses import dataclass


@dataclass(frozen=True)
class Kot:
    imie: str 
    wiek: int 

@dataclass(frozen=True) 
class Pies:
    imie: str
    rasa: str
@dataclass(frozen=True)
class Ksiazka:
    tytul: str
    strony: int

