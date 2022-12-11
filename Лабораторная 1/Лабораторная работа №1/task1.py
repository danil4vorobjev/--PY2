import doctest
from typing import Union

class Table:
    def __init__(self, height: Union[int, float], width: Union[int, float], thickness: Union[int, float]):
    """
    Создание и подготовка к работе в объекте Стол
    """
        if not isinstance(height, (int, float)):
            raise TypeError
        if not height > 0:
            raise ValueError
        self.height = height # Высота стола

        if not isinstance(width, (int, float)):
            raise TypeError
        if not width > 0:
            raise ValueError
        self.width = width # Ширина стола

        if not isinstance(thickness, (int, float)):
            raise TypeError
        if not thickness > 0:
            raise ValueError
        self.thickness = thickness # Толщина столешницы

    def height_change (self, value_change_height) -> int:
    """
    Метод позволяет изменить высоту стола
    в зависимости от пожелания заказчика,
    может принимать отрицательные значения,
    если нужно уменьшить высоту стола

    :return конечную высоту стола

    Пример:
    table = Table(900, 600, 35)
    table.height_change(100)
    """
    ...
    def width_change (self, value_change_width) -> int:
    """
    Метод позволяет изменить ширинуу стола
    в зависимости от пожелания заказчика,
    может принимать отрицательные значения,
    если нужно уменьшить ширину стола

    :return конечную ширину стола

    Пример:
    table = Table(900, 600, 35)
    table.width_change(50)
    """
    ...

if __name__ == "__main__":
    doctest.testmod()

class Keyboard:
    def __init__(self, color: str, language: str):
    """
    Создание и подготовка к работе в объекте Клавиатура
    """
        if not isinstance(color, (str)):
            raise TypeError
        self.color = color # Цвет подсветки

        if not isinstance(language, (str)):
            raise TypeError
        self.language = language # Язык раскладки

    def color_change (self, new_color) -> str:
    """
    Метод позволяет изменить цвет подсветки
    клавиатуры

    :return новый цвет

    Пример:
    keyboard = Keyboard(red, Russian)
    keyboard.color_change(blue)
    """
    ...
    def language_change (self, other_language) -> int:
    """
    Метод позволяет поменять языу раскладки

    :return язык ввода

    Пример:
    keyboard = Keyboard(red, Russian)
    keyboard.language_change(English)
    """
    ...

if __name__ == "__main__":
    doctest.testmod()

class Flat:
    def __init__(self, area: Union[int, float], cost: int):
        """
            Создание и подготовка к работе в объекте Квартира
            """
        if not isinstance(area, (int, float)):
            raise TypeError
        if not area > 0:
            raise ValueError
        self.area = area  # Площадь квартиры

        if not isinstance(cost, int):
            raise TypeError
        if not cost > 0:
            raise ValueError
        self.cost = cost  # Стоимость квартиры

    def price_square_meter(self, area, cost) -> int:
        """
        Метод позволяет расчитать цену за квадратный метр квартиры

        :return цена за квадратный метр

        Пример:
        table = Flat(40, 4500000)
        table.price_square_meter()
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()


