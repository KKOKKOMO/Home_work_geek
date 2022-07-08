# Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное,
# выводить только первые 10 букв в слове.

my_string = input().split()
print(my_string)

for i in range(len(my_string)):
    if len(my_string[i]) > 10:
        print(f'{i + 1}.{my_string[i][:10]}')
    else:
        print(f'{i + 1}. {my_string[i]}')
