class Student:
    """Класс студента"""

    def __init__(self, name, student_id):
        """Создает объект Student"""

        self.name = name
        self.student_id = student_id

    def study(self):
        """Выводит сообщение о том, что студент учится"""
        print(f"{self.name} учится")


class Teacher:
    """Класс преподавателя"""

    def __init__(self, name, subject):
        """Создает объект Teacher"""

        self.name = name
        self.subject = subject

    def teach(self):
        """Выводит сообщение о том, что преподаватель ведёт урок"""
        print(f"{self.name} преподает {self.subject}")


class Assistant(Student, Teacher):
    """Класс, представляющий ассистента, который является и студентом, и преподавателем и
    наследует функциональность от Student и Teacher"""

    def __init__(self, name, student_id, subject):
        """Создает объект Assistant"""

        Student.__init__(self, name, student_id)
        Teacher.__init__(self, name, subject)

    def help_student(self):
        """Выводит сообщение о том, что ассистент помогает студенту"""
        print(f"{self.name} помогает студенту с предметом {self.subject}")


# Пример
if __name__ == "__main__":
    assistant = Assistant("Артем", "123321", "Программирование на Python")
    assistant.study()
    assistant.teach()
    assistant.help_student()