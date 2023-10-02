def user_divide():
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        result = a / b
    except ValueError:
        print("Ошибка: некорректное значение. Попробуйте еще раз!")
        return user_divide()
    except ZeroDivisionError:
        print("Ошибка: деление на ноль! Используйте другое значение делителя.")
        return user_divide()
    return result

print(user_divide())