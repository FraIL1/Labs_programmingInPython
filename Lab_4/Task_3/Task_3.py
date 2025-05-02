from Lab_4.Task_1.Task_1 import NumberGuesser
from Lab_4.Task_2.Task_2 import Game
from Lab_4.Task_4.Task_4 import run_game


def main():
    while True:
        play = input('В какую игру хотите играть(Угадай число/ Блэкджэк/ Крестики-нолики/ Выход): ')

        if play == "Угадай число":
            game = NumberGuesser()
            game.play()
        elif play == "Блэкджэк":
            game = Game()
            game.start()
        elif play == "Крестики-нолики":
            run_game()
        elif play == "Выход":
            break
        else:
            print("Такой игры нет. Попробуй еще раз!")


if __name__ == "__main__":
    main()