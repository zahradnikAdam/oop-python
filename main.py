class Car:

    def __init__(self, znacka: str, rok: int, model: str, typ_prevodovky: str, barva: str, cena: float, vybava=None):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.typ_prevodovky = typ_prevodovky
        self.barva = barva
        self.cena = cena
        self.vybava = vybava if vybava else []

    def vypis(self):
        vybava_str = ", ".join([f"{v['nazev']} ({v['cena']} Kč)" for v in self.vybava]) if self.vybava else "žádná"
        return (
            f"Název auta: {self.znacka}, "
            f"Rok výroby: {self.rok}, "
            f"Model: {self.model}, "
            f"Typ převodovky: {self.typ_prevodovky}, "
            f"Barva: {self.barva}, "
            f"Cena s DPH: {self.cena} Kč, "
            f"Cena bez DPH: {self.cena_bez_dph()} Kč, "
            f"Příplatková výbava: {vybava_str}"
        )

    def cena_bez_dph(self):
        
        return round(self.cena / 1.21, 2)

def vyber_vybavu(vsechny_vybavy):
    print("Dostupné příplatkové výbavy:")
    for idx, vybava in enumerate(vsechny_vybavy):
        print(f"{idx+1}. {vybava['nazev']} ({vybava['cena']} Kč)")
    vyber = input("Zadej čísla vybraných výbav oddělená čárkou (např. 1,3): ")
    vybrane = []
    cisla = [int(x.strip()) - 1 for x in vyber.split(",") if x.strip().isdigit()]
    for i in cisla:
        if 0 <= i < len(vsechny_vybavy):
            vybrane.append(vsechny_vybavy[i])
    return vybrane


dostupne_vybavy = [
    {"nazev": "kožená sedadla", "cena": 35000},
    {"nazev": "panoramatická střecha", "cena": 25000},
    {"nazev": "sportovní paket", "cena": 50000},
    {"nazev": "adaptivní tempomat", "cena": 20000}
]


print("Vyber výbavu pro Audi:")
audi_vybava = vyber_vybavu(dostupne_vybavy)
audi = Car("Audi", 1999, "A4", "Manuální", "Stříbrná", 45000, audi_vybava)

print("\nVyber výbavu pro Škoda:")
skoda_vybava = vyber_vybavu(dostupne_vybavy)
skoda = Car("Škoda", 2014, "Superb II", "Manuální", "Bílá", 310000, skoda_vybava)

print("\nVyber výbavu pro BMW:")
bmw_vybava = vyber_vybavu(dostupne_vybavy)
bmw = Car("BMW", 2020, "X5", "Automatická", "Černá", 1200000, bmw_vybava)

auta = [audi, skoda, bmw]

for auto in auta:
    print("\n" + auto.vypis())