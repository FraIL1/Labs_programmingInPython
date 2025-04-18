class Student:
    def __init__(self, name, student_id):
        """Конфигурация студента"""

        self.name = name
        self.student_id = student_id
        self.grades = []  # пустой список оценок

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


    def display_info(self):
        """Вывожу результаты"""

        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {', '.join(map(str, self.grades))}")
        print(f"Средний балл: {self.get_average():.2f}\n")

# Пример
if __name__ == "__main__":
    # создаю студентов
    student1 = Student("Артем Иванов", "2025-001")
    student2 = Student("Влад Петров", "2025-002")

    # добавляю оценки
    student1.add_grade(8)
    student1.add_grade(7)
    student1.add_grade(9)

    student2.add_grade(10)
    student2.add_grade(6)
    student2.add_grade(8)
    student2.add_grade(7)


    print("Инфа о студентах:\n")
    student1.display_info()
    student2.display_info()

    # проверяю обработку ошибок
    try:
        student1.add_grade(11)
    except ValueError as i:
        print(f"Ошибка: {i}")