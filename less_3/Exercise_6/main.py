# Реализовать функцию int_func(),
# принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(some_word):
    return some_word[0].upper() + some_word[1:].lower()


some_list = []
curr_string = input('Input some words: ').split()
for i, word in enumerate(curr_string):
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('ERROR')
    else:
        curr_string[i] = int_func(word)
print(' '.join(curr_string))
