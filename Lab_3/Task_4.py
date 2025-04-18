class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._transactions = []

    def deposit(self, money):
        """Пополнение счета"""

        if money <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += money
        self._transactions.append(f"Пополнение: +{money}")

    def withdraw(self, money):
        """Снятие со счета"""

        if money <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if money > self._balance:
            raise ValueError("Недостаточно средств на счете")
        self._balance -= money
        self._transactions.append(f"Снятие: -{money}")

    @property
    def balance(self):
        """Геттер для текущего баланса"""
        return self._balance

    def get_transactions(self):
        """Получаю истории транзакций"""
        return self._transactions.copy()

# Пример
if __name__ == "__main__":
    # создаю новый счет с балансом 1000
    account = BankAccount(111)
    print(f"Мой баланс: {account.balance} рублей")

    # пополняю счет
    account.deposit(5555)
    print(f"Баланс после пополнения: {account.balance} рублей")

    # снимаю деньги
    account.withdraw(2222)
    print(f"Баланс после снятия: {account.balance} рублей")

    # снимаю больше, чем есть на счете
    try:
        account.withdraw(10000)
    except ValueError as i:
        print(f"Ошибка: {i}")

    # вношу отрицательную сумму
    try:
        account.deposit(-1000000)
    except ValueError as i:
        print(f"Ошибка: {i}")

    # вывожу историю операций
    print("\nИстория сделок:")
    for operation in account.get_transactions():
        print(operation)

    # проверяю текущий баланс
    print(f"\nТекущий баланс: {account.balance} руб")