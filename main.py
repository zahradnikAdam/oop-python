class Car:
    def __init__(self, znacka: str, rok: int, model: str, barva: str, typ_prevodovky: str, cena: float):
        self.znacka = str(znacka)
        self.rok = int(rok)
        self.model = str(model)
        self.barva = str(barva)
        self.typ_prevodovky = str(typ_prevodovky)
        self.cena = float(cena)
 
    def cena_bez_dph(self):
        return self.cena / 1.21
 
    def vypis(self):
        return (
            f"........................................\n"
            f"Název auta: {self.znacka}\n"
            f"Rok výroby: {self.rok}\n"
            f"Model: {self.model}\n"
            f"Barva: {self.barva}\n"
            f"Typ převodovky: {self.typ_prevodovky}\n"
            f"Cena: {self.cena:,.2f} Kč\n"
            f"Cena bez DPH: {self.cena_bez_dph():,.2f} Kč\n"
            f"........................................"
        )
 
 
skoda = Car("Škoda", 2021, "Octavia", "bílá", "manuální", 310000)
audi = Car("Audi", 2022, "A4", "černá", "automat", 450000)
 
seznam_aut = [
    Car("BMW", 2020, "X5", "modrá", "automat", 520000),
    Car("Audi", 2022, "Q7", "černá", "automat", 450000),
    Car("Škoda", 2021, "Superb", "bílá", "manuální", 310000),
    Car("Volkswagen", 2019, "Golf", "červená", "manuální", 280000),
    Car("Toyota", 2023, "Corolla", "bílá", "automat", 390000),
    Car("Ford", 2018, "Focus", "šedá", "manuální", 210000),
    Car("Mercedes-Benz", 2021, "C-Class", "černá", "automat", 610000),
    Car("Hyundai", 2022, "i30", "modrá", "manuální", 340000),
    Car("Kia", 2020, "Ceed", "zelená", "manuální", 295000),
    Car("Peugeot", 2019, "308", "bílá", "automat", 270000)
]
 
 
print(skoda.vypis())
print(audi.vypis())
 
for auto in seznam_aut:
    print(auto.vypis() + "-" * 40)