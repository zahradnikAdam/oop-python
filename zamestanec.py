class Zamestnanec:
    
    _id_counter = 1

    def __init__(self, jmeno, prijmeni, pozice, plat, oddeleni, vek):
      
        self.id = Zamestnanec._id_counter
        Zamestnanec._id_counter += 1
        self.jmeno = str (jmeno)
        self.prijmeni = str (prijmeni)
        self.pozice = str (pozice)
        self.plat = int (plat)
        self.oddeleni = oddeleni
        self.vek = int (vek)


    def cele_jmeno(self):
        """Vrací celé jméno zaměstnance."""
        return f"{self.jmeno} {self.prijmeni}"

    def zaspi(self):
        """S 50% pravděpodobností zaměstnanec zaspí."""
        import random
        if random.random() < 0.5:
            print(f"{self.cele_jmeno()} dnes zaspal!")
        else:
            print(f"{self.cele_jmeno()} přišel včas.")

    def zvys_plat(self, castka):
        """Zvýší plat zaměstnance o zadanou částku."""
        self.plat += castka

    def info(self):
        """Vrací textovou reprezentaci informací o zaměstnanci."""
        return (
            f"ID: {self.id}\n"
            f"Jméno: {self.cele_jmeno()}\n"
            f"Pozice: {self.pozice}\n"
            f"Plat: {self.plat} Kč\n"
            f"Oddělení: {self.oddeleni}\n"
            f"Věk: {self.vek} let\n"
        )

zamestnanci = [  # Seznam 10 zaměstnanců
    Zamestnanec("Jan", "Novák", "Programátor", 50000, "IT", 30),
    Zamestnanec("Petr", "Svoboda", "Analytik", 48000, "IT", 28),
    Zamestnanec("Lucie", "Dvořáková", "Účetní", 42000, "Finance", 35),
    Zamestnanec("Eva", "Králová", "HR Manažer", 53000, "HR", 40),
    Zamestnanec("Tomáš", "Bartoš", "Tester", 41000, "IT", 27),
    Zamestnanec("Anna", "Veselá", "Marketing", 45000, "Marketing", 32),
    Zamestnanec("Marek", "Kučera", "Obchodník", 47000, "Obchod", 38),
    Zamestnanec("Jana", "Procházková", "Asistentka", 35000, "Administrativa", 25),
    Zamestnanec("Michal", "Horák", "Správce sítě", 49000, "IT", 36),
    Zamestnanec("Barbora", "Benešová", "Projektový manažer", 60000, "Projekty", 41)
]

 
if __name__ == "__main__":
    
    print("--- Informace o zaměstnancích ---\n")
    for z in zamestnanci:
        print(z.info())
        print("-----------------------------")

    for z in zamestnanci:
        print(f"\nZaměstnanec: {z.cele_jmeno()}")
        vcas = input("Přišel zaměstnanec včas? (ano/ne): ").strip().lower()
        if vcas == "ano":
            print(f"{z.cele_jmeno()} přišel včas.")
        else:
            print(f"{z.cele_jmeno()} dnes zaspal!")

        chce_zvyseni = input("Chcete mu zvýšit plat ? (ano/ne): ").strip().lower()
        if chce_zvyseni == "ano":
            while True:
                try:
                    castka = int(input("O kolik Kč chcete zvýšit plat?: "))
                    z.zvys_plat(castka)
                    print(f"Plat zaměstnance {z.cele_jmeno()} byl zvýšen na {z.plat} Kč.")
                    break
                except ValueError:
                    print("Zadejte plat jako celé číslo!")
        else:
            print(f"Plat zaměstnance {z.cele_jmeno()} zůstává {z.plat} Kč.")
