import random


class Game:
    """ Класс, представляющий игру в Блэкджэк """

    def __init__(self):
        """ Создаем и перемешиваем колоду, раздаем начальные карты """

        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # Колода карт
        random.shuffle(self.deck)
        self.player = []  # Карты игрока
        self.dealer = []  # Карты дилера

    def deal_card(self) -> int:
        """ Раздаем одну карту из колоды """

        return self.deck.pop()  # с помощью list.pop() удаляем карту из колоды

    def calculate_score(self, cards: list) -> int:
        """ Вычисляем сумму очков карт """

        score = sum(cards)
        # Заменяем 11 на 1 если перебор
        if score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
        return score

    def start(self):
        """ Запускает игру Блэкджэк """
        print("Игра Блэкджэк!")
        print("Правила: набрать сумму очков ближе к 21 чем дилер, но не больше.\n")

        # Раздаем начальные карты
        self.player = [self.deal_card(), self.deal_card()]
        self.dealer = [self.deal_card(), self.deal_card()]

        # Ход игрока
        while True:
            player_score = self.calculate_score(self.player)
            print(f"\nВаши карты: {self.player}, сумма: {player_score}")
            print(f"Карта дилера: [{self.dealer[0]}, ?]")

            if player_score >= 21:
                break

            choice = input("Взять карту (взять) или остановиться (стоп)? ").lower()
            if choice == 'взять':
                self.player.append(self.deal_card())
            elif choice == 'стоп':
                break
            else:
                print("Некорректный ввод. Введите 'взять' или 'стоп'.")

        # Ход дилера
        player_score = self.calculate_score(self.player)
        dealer_score = self.calculate_score(self.dealer)

        while dealer_score < 17 and player_score <= 21:
            self.dealer.append(self.deal_card())
            dealer_score = self.calculate_score(self.dealer)

        # Результат игры
        print(f"\nВаши карты: {self.player}, сумма: {player_score}")
        print(f"Карты дилера: {self.dealer}, сумма: {dealer_score}")

        if player_score > 21:
            print("Перебор! Вы проиграли xd")
        elif dealer_score > 21:
            print("Дилер перебрал! Вы выиграли, Поздравляю!")
        elif player_score > dealer_score:
            print("Вы выиграли!")
        elif player_score < dealer_score:
            print("Вы проиграли")
        else:
            print("Ничья!")


if __name__ == "__main__":
    game = Game()
    game.start()