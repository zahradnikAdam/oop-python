class Car:
    def __init__(self, znacka: str, rok: int, model: str, barva: str, typ_prevodovky: str, cena: float, priplatkova_vybava=None):
        self.znacka = str(znacka)
        self.rok = int(rok)
        self.model = str(model)
        self.barva = str(barva)
        self.typ_prevodovky = str(typ_prevodovky)
        self.cena = float(cena)
        if priplatkova_vybava is None:
            self.priplatkova_vybava = []
        else:
            self.priplatkova_vybava = priplatkova_vybava
 
    def cena_bez_dph(self):
        return self.cena / 1.21
 
    def vypis(self):
        vybava = ", ".join(self.priplatkova_vybava) if self.priplatkova_vybava else "žádná"
        return (
            f"........................................\n"
            f"Název auta: {self.znacka}\n"
            f"Rok výroby: {self.rok}\n"
            f"Model: {self.model}\n"
            f"Barva: {self.barva}\n"
            f"Typ převodovky: {self.typ_prevodovky}\n"
            f"Cena: {self.cena:,.2f} Kč\n"
            f"Cena bez DPH: {self.cena_bez_dph():,.2f} Kč\n"
            f"Příplatková výbava: {vybava}\n"
            f"........................................"
        )
 
skoda = Car("Škoda", 2021, "Octavia", "bílá", "manuální", 310000)
skoda = Car("Škoda", 2021, "Octavia", "bílá", "manuální", 310000, ["navigace", "parkovací senzory"])
audi = Car("Audi", 2022, "A4", "černá", "automat", 450000, ["kožená sedadla", "panoramatická střecha"])

seznam_aut = [
    Car("BMW", 2020, "X5", "modrá", "automat", 520000, ["adaptivní tempomat", "head-up displej"]),
    Car("Audi", 2022, "Q7", "černá", "automat", 450000, ["masážní sedadla"]),
    Car("Škoda", 2021, "Superb", "bílá", "manuální", 310000, ["vyhřívaný volant"]),
    Car("Volkswagen", 2019, "Golf", "červená", "manuální", 280000, ["LED světlomety"]),
    Car("Toyota", 2023, "Corolla", "bílá", "automat", 390000, ["bezklíčové odemykání"]),
    Car("Ford", 2018, "Focus", "šedá", "manuální", 210000, ["parkovací kamera"]),
    Car("Mercedes-Benz", 2021, "C-Class", "černá", "automat", 610000, ["ventilovaná sedadla"]),
    Car("Hyundai", 2022, "i30", "modrá", "manuální", 340000, ["navigace"]),
    Car("Kia", 2020, "Ceed", "zelená", "manuální", 295000, ["panoramatická střecha"]),
    Car("Peugeot", 2019, "308", "bílá", "automat", 270000, ["vyhřívaná sedadla"])
]
 
 
print(skoda.vypis())
print(audi.vypis())
 
for auto in seznam_aut:
    print(auto.vypis() + "-" * 40)