import random
from datetime import datetime


class NumberGuesser:
    """ Класс для игры "Угадай число". Генерирует случайное число и позволяет пользователю угадывать его """

    def __init__(self):
        """ Запускает NumberGuesser, устанавливая случайное число, сбрасывая счетчик попыток и запоминая время начала игры """
        self.secret = random.randint(1, 30)  # Случайное число, которое нужно угадать (от 1 до 30)
        self.attempts = 0  # Количество попыток, сделанных пользователем
        self.start_time = datetime.now()  # Время начала игры

    def play(self):
        """
        Запускает цикл угадывания числа, пока пользователь не введет правильный ответ;
        Обрабатывает пользовательский ввод и дает подсказки (Больше или Меньше);
        При угадывании числа сохраняет статистику и завершает игру
        """
        print("Угадай число от 1 до 30!")
        while True:
            try:
                guess = int(input("Введите число: "))
                self.attempts += 1

                if guess < self.secret:
                    print("Больше!")
                elif guess > self.secret:
                    print("Меньше!")
                else:
                    time_spent = datetime.now() - self.start_time
                    self._save_stats(time_spent)
                    print(f"Число {self.secret} угадано за {self.attempts} попыток")
                    return
            except ValueError:
                print("Надо вводить только числа!")

    def _save_stats(self, time):
        """ Приватный метод для сохранения статистики игры в файл logs.txt """
        stats = (
            f"\nЗагадано: {self.secret}",
            f"Попыток: {self.attempts}",
            f"Время: {time.seconds} сек",
        )
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(stats) + "\n")


if __name__ == "__main__":
    game = NumberGuesser()
    game.play()