#  Программа запрашивает у пользователя строку чисел, разделённых пробелом.
#  При нажатии Enter должна выводиться сумма чисел.
#  Пользователь может продолжить ввод чисел,
#  разделённых пробелом и снова нажать Enter.
#  Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#  Но если вместо числа вводится специальный символ,
#  выполнение программы завершается.
#  Если специальный символ введён после нескольких чисел,
#  то вначале нужно добавить сумму этих чисел к полученной
#  ранее сумме и после этого завершить программу.
summa = 0
print('Напишите "stop", чтобы завершить программу иначе нажмите "ENTER"')
while True:
    my_str = input().split()
    if 'stop' not in my_str:
        numbers = map(int, my_str)
        for number in numbers:
            summa += number
        print(summa)
    elif 'stop' in my_str:
        for digit in my_str:
            try:
                summa += int(digit)
            except ValueError:
                print(summa)
        break