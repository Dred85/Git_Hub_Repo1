def get_capital_letters(user_line: str) -> str:
    """Функция для преобразования всех букв в заглавные"""
    return user_line.upper()


def get_title_letters(user_line: str) -> str:
    """Функция для преобразования первых букв в заглавные """
    return user_line.title()

print(get_title_letters('asf dsf fdf'))
