class person:
    _id_pocitadlo = 1

    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.id = person._id_pocitadlo
        person._id_pocitadlo += 1
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def Vypis(self):
        plat_info = ""
        if hasattr(self, 'pay_grade'):
            platova_trida_info = self.platova_trida()
            plat_info = f"Plat: {self.salary} Kč\n{platova_trida_info}\n"
        return (
            f"ID: {self.id}\n"
            f"Jméno: {self.name}\n"
            f"Příjmení: {self.surname}\n"
            f"Věk: {self.age}\n"
            f"Pohlaví: {self.gender}\n"
            f"{plat_info}"
        )

class student(person):
    def __init__(self, name: str, surname: str, age: int, gender: str, student_class):
        super().__init__(name, surname, age, gender)
        self.student_class = student_class

class employee(person):
    def __init__(self, name: str, surname: str, age: int, gender: str, salary: int, pay_grade: int):
        super().__init__(name, surname, age, gender)
        self.salary = int(salary)
        if pay_grade not in [10, 11, 12, 13]:
            raise ValueError("Platová třída musí být 10, 11, 12 nebo 13.")
        self.pay_grade = pay_grade

    def platova_trida(self):
        """Vrací platovou třídu zaměstnance a základní plat podle třídy."""
        zakladni_platy = {
            10: 32000,
            11: 35000,
            12: 38000,
            13: 42000
        }
        return f"Platová třída: {self.pay_grade}, Základní plat: {zakladni_platy[self.pay_grade]} Kč"
 

person_list = [
    employee("Petr", "Breit", 26, "Male", 42000, 10),
    employee("Lenka", "Zedníková", 41, "Female", 36000, 11),
    employee("Petr", "Leba", 46, "Male", 42000, 12),
    student("Daniel", "Polan", 18, "Male", "IT3A"),
    student("Martin", "Šedivec", 19, "Male", "IT3A"),
    student("Jakub", "Kořínský", 18, "Male", "IT4B"),
]

for zam in person_list:
    print(zam.Vypis())
    print("----------------------")