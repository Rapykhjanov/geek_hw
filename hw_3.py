class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        addition = self.__cpu + self.__memory
        subtraction = self.__cpu - self.__memory
        multiplication = self.__cpu * self.__memory
        division = self.__cpu / self.__memory if self.__memory != 0 else "Деление на ноль невозможно"
        return {
            "addition": addition,
            "subtraction": subtraction,
            "multiplication": multiplication,
            "division": division
        }

    def __str__(self):
        return f'CPU: {self.__cpu}, MEMORY: {self.__memory}'

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            operator_name = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {operator_name}")
        else:
            print("Ошибка: указан неверный номер сим-карты.")

    def __str__(self):
        return f'SIM CARDS: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}")

    def __str__(self):
        return f'{Computer.__str__(self)}, {Phone.__str__(self)}'


phone = Phone(["Beeline", "MegaCom"])
phone.call(1, "+996 777 99 88 11")
print(phone)

computer = Computer(4, 8)
print(computer.make_computations())
print(computer)

smartphone1 = SmartPhone(2, 5, ["Beeline", "MegaCom"])
smartphone2 = SmartPhone(4, 8, ["Beeline", "MegaCom"])
print(smartphone1)
smartphone1.use_gps("Bishkek")
smartphone2.use_gps("Batken")

print(smartphone1 < smartphone2)
print(smartphone1 > smartphone2)
print(smartphone1 == smartphone2)
print(smartphone1 != smartphone2)
print(smartphone1 <= smartphone2)
print(smartphone1 >= smartphone2)