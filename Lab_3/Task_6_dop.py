class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Геттер для температуры в градусах цельсия"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Сеттер для температуры в градусах Цельсия с валидацией"""
        if not isinstance(value, (int, float)):
            raise ValueError("Температура должна быть числом")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Геттер для температуры в градусах фаренгейта"""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Динамическое св-во для температуры в градусах фаренгейта"""
        if not isinstance(value, (int, float)):
            raise ValueError("Температура должна быть числом")
        self._celsius = (value - 32) * 5 / 9


# Пример
if __name__ == "__main__":

    # создаем объект с температурой 0
    temp = Temperature(0)
    print(f"0°C = {temp.fahrenheit}°F")

    # меняю температуру через свойство celsius
    temp.celsius = 100
    print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

    # Меняем температуру через свойство fahrenheit
    temp.fahrenheit = 40
    print(f"{temp.fahrenheit}°F = {temp.celsius}°C")

    # устанавливаю нечисловое значение
    try:
        temp.celsius = "20 градусов"
    except ValueError as e:
        print(f"Ошибка: {e}")