text = ['Привет\n', 'как дела?\n', 'что делаешь?\n']

with open("your_file2.txt", "w", encoding='utf-8') as file:
    for line in text:
        file.write(line)
