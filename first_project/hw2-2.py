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

secret_letters_list = []

# получаем список из списка списков
for words in secret_letter:
    for word in words:
        secret_letters_list.append(word)


# записываем в список только маленькие кириллические буквы
secret_words_list = [''.join(small_rus for small_rus in string if 'а' <= small_rus <= 'я')
                     for string in secret_letters_list]

# получаем строку, убираем запятые, пишем с большой буквы
secret_words = ' '.join(secret_words_list).capitalize()

print(secret_words)

input('Для выхода из программы нажмите Enter')
