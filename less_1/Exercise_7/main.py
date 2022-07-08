result_first_day = int(input('Введите результаты пробежки первого дня в км: '))
final_result = int(input('Введите общий желаемый результат в км: '))
curr_result = result_first_day
curr_day = 1
print(f'{curr_day}-й день: {curr_result}')
while curr_result <= final_result:
    curr_day += 1
    curr_result *= 1.1
    print(f'{curr_day}-й день: {curr_result:0.2f}')

# start, stop, step = 1, 1000, 1.00000053
# x = start
# sum = 0
# while x < stop:
#         sum += x
#         x *= step
# print(round(sum))







