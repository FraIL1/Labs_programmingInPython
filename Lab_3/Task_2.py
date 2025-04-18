class Person:
    """Создаю студента"""
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    """Создаю учителя"""
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        """Добавляю студента в список студентов преподавателя"""

        if student not in self.students:
            self.students.append(student)
            print(f"Студент {student.name} добавлен к преподавателю {self.name}\n")
        else:
            print(f"Студент {student.name} уже есть в списке")

    def remove_student(self, student):
        """Удаляю студента из списка студентов преподавателя"""

        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} удалён из списка преподавателя {self.name}\n")
        else:
            print(f"Студента {student.name} нет в списке")

    def list_students(self):
        """Вывожу список всех студентов преподавателя"""

        if not self.students:
            print(f"У преподавателя {self.name} пока нет студентов\n")
        else:
            print(f"Список студентов преподавателя {self.name}:")
            for student in self.students:
                print(f"- {student.name}")


# Пример
if __name__ == "__main__":

    # создаю несколько студентов
    student1 = Person("Артем Иванов", 21)
    student2 = Person("Влад Петров", 20)
    student3 = Person("АААА АААА", 19)

    # Создаём преподавателя
    teacher = Teacher("Алексей Николаев", 40, "Математика")

    # Добавляем студентов
    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.add_student(student3)

    # Выводим список студентов
    teacher.list_students()

    # Удаляем студента
    teacher.remove_student(student3)

    # Проверяем список после удаления
    teacher.list_students()