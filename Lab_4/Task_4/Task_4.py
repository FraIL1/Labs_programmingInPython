class GridGame:
    """ Класс, представляющий игровое поле и логику игры """

    def __init__(self):
        """ Игра с пустым полем """
        self.cells = [' '] * 9  # Список, представляющий игровое поле 3x3
        self.current_symbol = 'X'  # X всегда ходит первым

    def display(self):
        """
        Отображаем текущее состояние игрового поля в консоли;
        Нумерация клеток соответствует цифровой клавиатуре
        """

        visual = []
        for i in range(0, 9, 3):
            visual.append(f" {self.cells[i]} │ {self.cells[i + 1]} │ {self.cells[i + 2]} ")
            if i < 6:
                visual.append("───┼───┼───")
        print('\n'.join(visual))

    def make_turn(self, position):
        """ Выполняет ход в указанную позицию """

        idx = position - 1  # Конвертируем в индекс списка (0-8)
        if self.cells[idx] == ' ':
            self.cells[idx] = self.current_symbol
            return True  # True, если ход выполнен успешно
        return False  # False если позиция занята

    def switch_player(self):
        """ Переключает текущего игрока """

        self.current_symbol = 'O' if self.current_symbol == 'X' else 'X'

    def check_result(self):
        """ Проверяем состояние игры на наличие победителя или ничьи """

        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
            [0, 4, 8], [2, 4, 6]  # Диагонали
        ]

        for line in lines:
            a, b, c = line
            if self.cells[a] == self.cells[b] == self.cells[c] != ' ':
                return self.cells[a]  # Возвращаем символ победителя

        return 'Draw' if ' ' not in self.cells else None  # Ничья или игра продолжается


def show_instructions():
    print("\nИнструкция:")
    print("Введите число от 1 до 9, смотря на поле:")
    print(" 1 │ 2 │ 3 ")
    print("───┼───┼───")
    print(" 4 │ 5 │ 6 ")
    print("───┼───┼───")
    print(" 7 │ 8 │ 9 \n")


def run_game():
    """ Запускает игру """

    print("Крестики-нолики")
    game = GridGame()
    show_instructions()

    while True:
        game.display()

        try:
            choice = int(input(f"Игрок {game.current_symbol}, ваш ход: "))
            if not 1 <= choice <= 9:
                print("Пожалуйста, число от 1 до 9!")
                continue

            if not game.make_turn(choice):
                print("Эта позиция уже занята!")
                continue

            result = game.check_result()
            if result:
                game.display()
                if result == 'Draw':
                    print("\nИгра завершилась! Ничья!")
                else:
                    print(f"\nИгрок {result} одержал победу!")
                break

            game.switch_player()

        except ValueError:
            print("Нужно ввести число!")


if __name__ == "__main__":
    run_game()
