# from art import text2art
# # Стилизованный вывод текста
# art_text = text2art("Hello world!!!")
# print(art_text)


from art import text2art, randart

# Псевдослучайно выбранный стиль из доступных
art_text = randart()
print(art_text)

# Использование нескольких стилевых слоёв
top_art = text2art("Up")
bottom_art = text2art("Down")
print(top_art + bottom_art)

# Использование нескольких текстов в одном стиле
code_art_1 = text2art("def example():")
code_art_2 = text2art("    print('Hello')")
code_art_3 = text2art("example()")
print(code_art_1 + code_art_2 + code_art_3)
