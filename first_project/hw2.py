# Секретное послание
secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
                 ['оafбasdf%^о^FFжа$#af243ю'], ['afпFsfайFтFsfо13н'],
                 ['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
                 ['и$##sfF'], ['вSFSDам'], ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
                 ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]

# Список с маленькими русскими буквами
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
             'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

secret_words_list = []

for words in secret_letter:
    for word in words:
        secret_words_list.append(word)

sorted_words_list = []

for string in secret_letters_list:
    secret_words = ''.join(small_rus for small_rus in string if 'а' <= small_rus <= 'я')


# for i in range(len(secret_words_list)):
#     for letter in secret_words_list[i]:
#         if small_rus in secret_words_list:
#             sorted_words[i].append(small_rus[letter])

# print(sorted_words)

# secret_words = ' '.join(secret_words_list)
#
# print(secret_words)
# sorted_letters =''
#
# for letter in secret_words:
#     if small_rus[letter] in secret_words:
#         sorted_letters.append(letter)



# for word in secret_letter:



# for letter in secret_letter:
#     if small_rus[letter] in secret_letter:
#         sorted_letters.append(letter)

# for letter in range(int(secret_letter[i])):
#     if secret_letter[i] == secret_letter[i]:
#         sorted_letters.append(secret_letter[i])

# print(sorted_letters)


# Вот что у меня получилось

# ВВЕДИТЕ ТУТ ВАШ КОД
