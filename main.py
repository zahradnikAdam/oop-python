class car:

    def __init__(self, znacka: str, rok: int, model,typ_prevodovky: str,barva: str, cena: float):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena
        self.barva = barva

    def Vypis(self):
          return f"Název auta: {self.znacka}, Rok výroby: {self.rok}"
        

audi = car("Audi", 1999, "A4", "stříbrná", "Manuální", 45000)
skoda = car("Škoda", 2014, "superb 11", "Bílá", "Manuální", 310000)

print(audi.cena)
print(skoda.model)
print(audi.Vypis())