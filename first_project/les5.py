word_for_check = input("Введите слово для проверки: ")
count_r = 0

for char in word_for_check:
    if char.lower() == 'р':
        count_r += 1

if count_r == 0:
    print(f' Слово {word_for_check} хорошее!')
elif 0 < count_r < 3:
    print(f'Слово {word_for_check} плохое')
else:
    print(f' Здесь целых {count_r} буквы "р"')

