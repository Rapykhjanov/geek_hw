class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Полное имя: {self.full_name}')
        print(f'Возраст: {self.age}')
        if self.is_married.lower() == 'да':
            print('Женат')
        elif self.is_married.lower() == 'нет':
            print('Не женат')
        else:
            print("Введите корректный ответ (да/нет)")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_grade(self):
        if not self.marks:
            return "Нет оценок для расчета средней."
        total = sum(float(grade) for grade in self.marks.values())
        average = total / len(self.marks)
        return f'Средняя оценка: {average:.2f}'

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Оценки: {self.marks}')
        print(self.average_grade())


class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        extra_years = max(0, self.experience - 3)
        bonus = extra_years * 0.05 * Teacher.base_salary
        total_salary = Teacher.base_salary + bonus
        return total_salary

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Опыт работы: {self.experience} лет')
        print(f'Базовая зарплата: {Teacher.base_salary} KGS')
        print(f'Итоговая зарплата: {self.calculate_salary()} KGS')


def create_students():
    students = []
    for _ in range(3):
        name = input('Введите полное имя ученика: ').title()
        age = int(input('Введите возраст ученика: '))
        is_married = input('Ученик в браке (да/нет): ').title()
        marks = { }

        while True:
            subject = input('Введите название урока или (стоп) для завершения программы: ')
            if subject.lower() == "стоп":
                break
            grade = input(f'Введите оценку для {subject}: ')
            marks[subject] = grade

        students.append(Student(name, age, is_married, marks))

    return students


students = create_students()
for student in students:
    print("\nИнформация о студенте:")
    student.introduce_myself()

teacher_name = input('\nВведите полное имя учителя: ').title()
teacher_age = int(input('Введите возраст учителя: '))
teacher_is_married = input('Учитель в браке (да/нет): ').title()
experience = int(input('Введите стаж учителя в годах: '))

teacher = Teacher(teacher_name, teacher_age, teacher_is_married, experience)
print("\nИнформация о учителе:")
teacher.introduce_myself()