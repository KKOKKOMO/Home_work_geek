number = int(input('Enter number: '))
max_digit = number % 10
while number > 1:
    number //= 10
    if number % 10 > max_digit:
        max_digit = number % 10
    if max_digit == 9:
        break
print(f'Max digit in number is {max_digit}')
