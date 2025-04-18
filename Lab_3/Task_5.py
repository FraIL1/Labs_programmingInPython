class Student:
    def __init__(self, name, student_id):
        """Конфигурация студента"""

        self.name = name
        self.student_id = student_id
        self.grades = []  # Начальный пустой список оценок

    def add_grade(self, grade):
        """Добавляю оценку с проверкой допустимости"""

        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("Оценка должна быть от 0 до 10")

    def get_average(self):
        """Рассчитываю средний балл студента"""

        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Студент {self.name} (ID: {self.student_id})"

    def __eq__(self, other):
        """Сравниваю студентов по ID"""

        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __len__(self):
        """Кол-во оценок студента"""
        return len(self.grades)


    def display_info(self):
        """Вывожу результаты"""
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {', '.join(map(str, self.grades))}")
        print(f"Средний балл: {self.get_average():.2f}\n")

        print(student1)
        print(f"Количество оценок: {len(student1)}")

        print(f"\nСравнение студентов:")
        print(f"student1 == student2: {student1 == student2}")
        print(f"student1 == student3: {student1 == student3}")
        print(f"student1 == 'не студент': {student1 == 'не студент'}\n")


# Пример
if __name__ == "__main__":
    # создаю студентов
    student1 = Student("Артем Иванов", "2025-001")
    student2 = Student("Влад Петров", "2025-002")
    student3 = Student("АААА АААА", "2025-001")

    # добавляю оценки
    student1.add_grade(8)
    student1.add_grade(7)
    student1.add_grade(9)

    student2.add_grade(10)
    student2.add_grade(6)
    student2.add_grade(8)

    print("\nПолная инфа о студентах:\n")
    student1.display_info()
    student2.display_info()