# def outer_function():
#     outer_var = "I'm in the outer function."
#
#     def inner_function():
#         nonlocal outer_var
#         outer_var = "I'm modified in the inner function."
#         print(outer_var)
#
#     inner_function()
#
#
# outer_function()


class NegativeNumberError(Exception):
    pass


def sqrt(number):
    if number < 0:
        raise NegativeNumberError("Нельзя извлекать корень из отрицательного числа!")
    return number**(0.5)

try:
    print(sqrt(4))
except NegativeNumberError as e:
    print(e)
